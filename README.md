# Demo Python Plugin

Mini-Demo für die **MB Planungs-Toolbox** — eine „Projekt Übersicht"-Karte, deren Logik in
**echtem Python** läuft, via **Pyodide** (Python als WebAssembly **im Browser**). Eine einzige
`index.html`, kein Server nötig.

- **Tech:** `python` (Badge: gelb `PY`)
- **Hosting:** `static` → GitHub Pages (Pyodide macht Python statisch hostbar)
- **Daten:** nur synthetisch (C0/C1)

> **Hinweis zur Architektur:** Eine **produktive** Python-App (Streamlit/Flask) braucht einen
> **Server** — dann `"hosting": "server"` und `url` auf die Server-Adresse. Pyodide wird hier nur
> verwendet, damit die Demo ohne Server auf GitHub Pages läuft.

Live unter `https://cbcmlt.github.io/demo-python/`.
