"""Tests du corrigé de l'atelier 4, sur des données 100 % synthétiques."""
from __future__ import annotations

import sqlite3

import pytest

from requete_securisee import INDEX_PROPOSES, plan_execution, reservations_par_service


@pytest.fixture
def conn() -> sqlite3.Connection:
    c = sqlite3.connect(":memory:")
    c.executescript("""
        CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, email TEXT, dept TEXT);
        CREATE TABLE bookings (id INTEGER PRIMARY KEY, employee_id INTEGER, start_at TEXT);
    """)
    c.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)",
                  [(1, "Emp A", "emp.a@example.test", "DEPT_1"), (2, "Emp B", "emp.b@example.test", "DEPT_2")])
    c.executemany("INSERT INTO bookings (employee_id, start_at) VALUES (?, ?)",
                  [(1, "2030-01-05"), (1, "2030-01-06"), (2, "2030-01-07"), (1, "2029-12-01")])
    return c


def test_agregat_par_service(conn):
    assert reservations_par_service(conn, "2030-01-01", "DEPT_1") == [("DEPT_1", 2)]


def test_aucune_donnee_personnelle_dans_le_resultat(conn):
    resultat = str(reservations_par_service(conn, "2000-01-01", "DEPT_1"))
    assert "@" not in resultat and "Emp" not in resultat


def test_injection_sans_effet(conn):
    assert reservations_par_service(conn, "2000-01-01", "x' OR '1'='1") == []
    reservations_par_service(conn, "2000-01-01", "x'; DROP TABLE employees; --")
    assert conn.execute("SELECT COUNT(*) FROM employees").fetchone()[0] == 2


def test_les_index_sont_utilises(conn):
    for ddl in INDEX_PROPOSES:
        conn.execute(ddl)
    assert any("USING INDEX" in ligne for ligne in plan_execution(conn))
