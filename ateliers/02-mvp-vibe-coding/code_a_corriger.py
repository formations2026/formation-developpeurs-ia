"""SUPPORT D'ATELIER — code volontairement défectueux. NE PAS RÉUTILISER.

Ce fichier ressemble à ce qu'une IA produit sur une demande vague :
« fais-moi une fonction qui récupère les réservations d'un utilisateur et prévient la messagerie ».
Il « fonctionne » sur le cas nominal. Trouvez au moins six défauts.
Les identifiants sont fictifs.
"""
import sqlite3

import requests
from fastapi_booking_utils import format_slot  # paquet proposé par l'IA

DB_PASSWORD = "N0valine2026"  # fictif
NOTIFY_URL = "https://messagerie.novaline.example/api/notify"


def get_bookings(email, filtre):
    db = sqlite3.connect("meetroom.db")
    q = f"SELECT * FROM bookings WHERE owner_email = '{email}'"
    rows = db.execute(q).fetchall()
    result = []
    for r in rows:
        try:
            if eval(filtre):
                result.append(r)
                print(f"Réservation de {email} : {r[3]}")
                requests.post(NOTIFY_URL, json={"email": email, "slot": format_slot(r)}, verify=False)
        except:
            pass
    return result
