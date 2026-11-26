"""Point d'entrée de l'API MeetRoom.

Lancer : uvicorn app.main:app --reload     Documentation : http://127.0.0.1:8000/docs
"""
from __future__ import annotations

from fastapi import FastAPI

from app.routers import bookings, rooms

app = FastAPI(
    title="MeetRoom",
    version="1.0.0",
    description="Réservation de salles de réunion — application fil rouge de la formation.",
)
app.include_router(rooms.router)
app.include_router(bookings.router)


@app.get("/health", tags=["technique"])
def health() -> dict[str, str]:
    """Sonde de disponibilité."""
    return {"status": "ok"}
