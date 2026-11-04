# Soban Khan — Data Analyst & Python Developer

A responsive portfolio built with Python, Flask, Jinja2, HTML, CSS, and vanilla JavaScript. The two Power BI reports are presented as practice / learning projects, not commercial client work.

## Architecture

```text
.
├── app.py                    # Flask routes and portfolio content
├── requirements.txt          # Python dependencies
├── templates/
│   ├── base.html             # Shared layout, navigation, and footer
│   ├── index.html            # Portfolio sections
│   ├── project.html          # Reusable project-detail page
│   └── macros.html           # Reusable section heading and project card
└── static/
    ├── css/style.css         # Responsive visual design
    ├── js/main.js            # Accessible mobile navigation
    ├── images/               # Optional dashboard screenshots
    └── pdfs/                 # Original dashboard PDFs embedded on project pages
```

`app.py` owns the two public routes (`/` and `/projects/<slug>`) and the content data rendered by Jinja. The project detail route looks up a known project and returns a 404 for an unknown slug. `base.html` supplies shared metadata, navigation, and footer; `macros.html` avoids duplicating repeated headings and cards. Static assets are kept separate from templates.

## Dashboard PDFs

The supplied original PDFs and their rendered dashboard previews are included:

- `static/pdfs/sales-profit-analysis.pdf` — original copied from `Untitled.pdf`
- `static/images/sales-profit-dashboard.png` — preview rendered from that PDF
- `static/pdfs/superstore-sales-profit.pdf` — original copied from `professional_dashBoard.pdf`
- `static/images/superstore-dashboard.png` — preview rendered from that PDF

The project cards show the dashboard previews. Each project detail page displays its preview directly for compatibility across desktop and mobile browsers, and links to open the original PDF in a new tab. The UnitPrice dashboard is not included.
## Run locally

Python 3.9 or newer is recommended.

1. (Optional) Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install Flask:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. Start the development server from this directory:

   ```powershell
   py app.py
   ```

4. Open <http://127.0.0.1:5000/>.

The server listens on port `5000` and all network interfaces by default, so a phone on the same Wi-Fi can also connect using the computer's local IP address, for example `http://192.168.1.10:5000/`. Windows Firewall may ask permission for Python; allow access only on a trusted private network. Override the defaults with the `HOST` and `PORT` environment variables. Debug mode is off by default; set `FLASK_DEBUG=1` only during local development.

The Flask development server is for local testing. For deployment, use a production WSGI server and keep debug mode off.

## Pages and contact

- `/` — portfolio home page with About, Skills, Projects, Services, and Contact sections.
- `/projects/sales-profit-analysis` — Sales and Profit Analysis practice project.
- `/projects/superstore-analysis` — Superstore Sales and Profit practice project.

The email link opens the visitor's mail application; there is no contact form or server-side email delivery configured. GitHub links point to the profile supplied by Soban.
