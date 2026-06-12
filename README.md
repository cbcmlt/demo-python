# Demo Python Plugin

Mini-Demo für die **MB Planungs-Toolbox** — eine „Projekt Übersicht" als **echte Python-App**
mit **Streamlit**. Reines Python, **kein HTML** — läuft auf einem **Server** (GitHub Pages kann
kein Python ausführen).

- **Tech:** `python` (Badge: gelb `PY`)
- **Hosting:** `server` (Streamlit/Flask brauchen eine Laufzeit)
- **Daten:** nur synthetisch (C0/C1)

## Lokal starten

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployen (Server)

- **Streamlit Community Cloud:** Repo verbinden → liefert eine URL `https://<name>.streamlit.app/`.
- **Intern:** auf einem Windows-/Linux-Server bzw. Container hosten.

Danach die echte URL in der Registry eintragen: `cbcmlt/plugins/demo-python/plugin.json` → `url`.
