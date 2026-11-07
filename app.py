"""Flask application for Soban Khan's data analytics portfolio."""

from datetime import datetime
import os
from pathlib import Path

from flask import Flask, abort, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "number": "01",
        "slug": "sales-profit-analysis",
        "title": "Sales & Profit Analysis",
        "short_title": "Sales and Profit Analysis Dashboard",
        "label": "Practice project",
        "image": "images/sales-profit-dashboard.png",
        "pdf": "pdfs/sales-profit-analysis.pdf",
        "overview": (
            "A Power BI practice dashboard exploring how sales, profit, and units "
            "sold vary across countries and products."
        ),
        "objective": (
            "Explore sales and profitability across countries and products, and "
            "understand how different products and markets contribute to overall sales."
        ),
        "features": [
            "Sales and profit by country",
            "Units sold by country",
            "Sales and units sold by product",
            "Sales and profit comparison",
            "Sales trends across years",
        ],
        "observations": (
            "The report is structured to compare country- and product-level measures "
            "and to explore changes across years. No commercial conclusions or "
            "verified business results are claimed."
        ),
        "learning": (
            "Practiced organizing related sales measures into a single report and "
            "using geographic, product, and time-based views to explore the same dataset."
        ),
        "tools": ["Power BI"],
    },
    {
        "number": "02",
        "slug": "superstore-analysis",
        "title": "Superstore Sales & Profit",
        "short_title": "Superstore Sales and Profit Analysis Dashboard",
        "label": "Practice project",
        "image": "images/superstore-dashboard.png",
        "pdf": "pdfs/superstore-sales-profit.pdf",
        "overview": (
            "A Power BI learning project focused on category and sub-category "
            "sales, quantity, and profitability over time."
        ),
        "objective": (
            "Explore category-level and sub-category-level sales and profitability "
            "to identify differences in performance."
        ),
        "features": [
            "Sales by category",
            "Quantity by category",
            "Profit by category",
            "Profit by sub-category",
            "Sales over order dates",
            "Overall category profit distribution",
        ],
        "observations": (
            "The dashboard brings category and sub-category measures together so "
            "they can be compared alongside order-date trends. No verified business "
            "impact or unsupported numeric findings are presented."
        ),
        "learning": (
            "Practiced comparing measures at multiple levels of detail and arranging "
            "time-based and category-based views into one report."
        ),
        "tools": ["Power BI"],
    },
]

SKILL_GROUPS = [
    {"name": "Programming", "skills": ["Python", "Flask"]},
    {
        "name": "Data analysis",
        "skills": ["Pandas", "NumPy", "Data cleaning", "Data analysis"],
    },
    {
        "name": "Visualization",
        "skills": ["Power BI", "Matplotlib", "Seaborn"],
    },
    {"name": "Tools & workflow", "skills": ["SQL · learning", "Git", "GitHub"]},
]

SERVICES = [
    "Data cleaning",
    "Exploratory data analysis",
    "Excel / CSV data processing",
    "Power BI dashboard development",
    "Business data visualization",
    "Python automation",
]


@app.context_processor
def inject_site_details():
    """Make shared profile details and the current year available to templates."""
    return {
        "current_year": datetime.now().year,
        "github_url": "https://github.com/sobankhan169910-cell",
        "email_address": "sobankbai@gmail.com",
        "whatsapp_number": "03555282740",
        "whatsapp_url": "https://wa.me/923555282740",
    }


@app.get("/")
def home():
    image_directory = Path(app.static_folder) / "images"
    projects = [
        {
            **project,
            "image_available": (image_directory / project["image"].split("/")[-1]).is_file(),
            "pdf_available": (Path(app.static_folder) / project["pdf"]).is_file(),
        }
        for project in PROJECTS
    ]
    return render_template(
        "index.html",
        projects=projects,
        skill_groups=SKILL_GROUPS,
        skill_count=sum(len(group["skills"]) for group in SKILL_GROUPS),
        max_skill_group_size=max(len(group["skills"]) for group in SKILL_GROUPS),
        services=SERVICES,
        profile_image_available=(image_directory / "profile.png").is_file(),
    )


@app.get("/projects/<slug>")
def project_detail(slug):
    project = next((item for item in PROJECTS if item["slug"] == slug), None)
    if project is None:
        abort(404)

    image_path = Path(app.static_folder) / "images" / project["image"].split("/")[-1]
    pdf_path = Path(app.static_folder) / project["pdf"]
    return render_template(
        "project.html",
        project={
            **project,
            "image_available": image_path.is_file(),
            "pdf_available": pdf_path.is_file(),
        },
    )


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true"},
    )
