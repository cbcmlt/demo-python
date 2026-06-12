"""Projekt Übersicht — Demo-Plugin (Streamlit, serverbasiert).

Echte Python-App: läuft mit `streamlit run app.py` auf einem Server
(GitHub Pages kann kein Python ausführen).
Nur synthetische Daten (R_86: C0) — keine personenbezogenen Daten.
"""

import random

import streamlit as st

PROJECTS = ["B-Tunnel Nord", "Brückenfeld Süd", "Halle 7 Ausbau", "Trasse West"]
STATES = ["In Planung", "In Ausführung", "Abnahme", "Abgeschlossen"]

st.set_page_config(page_title="Projekt Übersicht — Demo Python", layout="centered")

st.title("Projekt Übersicht  🐍")
st.caption("Demo-Plugin — Streamlit (Python)")

if st.button("Aktualisieren"):
    st.session_state["seed"] = random.random()

rng = random.Random(st.session_state.get("seed", 0.42))
project = rng.choice(PROJECTS)
status = rng.choice(STATES)
progress = rng.randint(0, 100)

col1, col2 = st.columns(2)
col1.metric("Projekt", project)
col2.metric("Status", status)

st.metric("Fortschritt", f"{progress}%")
st.progress(progress / 100)
