"""CORRIGÉ — atelier 4 : la requête après le workflow sécurisé.

Changements par rapport à requete_a_securiser.py :
- plus aucun identifiant de connexion dans le code (fourni par l'appelant, depuis l'environnement) ;
- requête paramétrée : plus d'injection possible ;
- minimisation : un agrégat par service, sans nom ni e-mail (le classement nominatif n'était pas nécessaire) ;
- index proposés, à valider avec le plan d'exécution sur une copie anonymisée.

Paramètres nommés `:nom` : syntaxe SQLite (démonstration et tests). Avec PostgreSQL et psycopg,
la même requête s'écrit avec `%(debut)s` et `%(service)s` ; le principe est identique.
"""
from __future__ import annotations

import sqlite3

REQUETE = (
    "SELECT e.dept, COUNT(*) AS nb "
    "FROM bookings b JOIN employees e ON e.id = b.employee_id "
    "WHERE b.start_at >= :debut AND e.dept = :service "
    "GROUP BY e.dept"
)

INDEX_PROPOSES = (
    "CREATE INDEX IF NOT EXISTS idx_bookings_start ON bookings(start_at)",
    "CREATE INDEX IF NOT EXISTS idx_bookings_employee ON bookings(employee_id)",
    "CREATE INDEX IF NOT EXISTS idx_employees_dept ON employees(dept)",
)


def reservations_par_service(conn: sqlite3.Connection, debut: str, service: str) -> list[tuple[str, int]]:
    """Nombre de réservations d'un service depuis `debut` (ISO 8601). Aucun nom, aucun e-mail."""
    rows = conn.execute(REQUETE, {"debut": debut, "service": service}).fetchall()
    return [(str(r[0]), int(r[1])) for r in rows]


def plan_execution(conn: sqlite3.Connection) -> list[str]:
    """Plan d'exécution de la requête (SQLite) : à lire avant toute exécution sur de vraies données."""
    rows = conn.execute("EXPLAIN QUERY PLAN " + REQUETE, {"debut": "", "service": ""}).fetchall()
    return [str(r[-1]) for r in rows]
