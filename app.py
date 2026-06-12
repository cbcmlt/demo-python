"""Projekt Übersicht — Demo-Logik in Python.

Läuft via Pyodide (WebAssembly) im Browser, wird von index.html geladen.
Nur synthetische Daten (R_86: C0) — keine personenbezogenen Daten.
"""

import json
import random

PROJECTS = ["B-Tunnel Nord", "Brückenfeld Süd", "Halle 7 Ausbau", "Trasse West"]
STATES = ["In Planung", "In Ausführung", "Abnahme", "Abgeschlossen"]


def uebersicht() -> str:
    """Liefert eine zufällige Projektübersicht als JSON-String."""
    return json.dumps({
        "project": random.choice(PROJECTS),
        "status": random.choice(STATES),
        "progress": random.randint(0, 100),
    })
