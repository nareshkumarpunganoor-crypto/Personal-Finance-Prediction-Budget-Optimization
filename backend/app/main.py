"""
Main FastAPI application entry point for Personal Finance Prediction API.
"""

import sys
import os

# Fix import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings

# Frontend path
FRONTEND_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "frontend"
)
print(f"Frontend dir    : {FRONTEND_DIR}")
print(f"Frontend exists : {os.path.exists(FRONTEND_DIR)}")

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="Personal Finance Prediction & Budget Optimization API"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
css_dir = os.path.join(FRONTEND_DIR, "css")
js_dir  = os.path.join(FRONTEND_DIR, "js")

if os.path.exists(css_dir):
    app.mount("/css", StaticFiles(directory=css_dir), name="css")
    print(f"CSS mounted from: {css_dir}")

if os.path.exists(js_dir):
    app.mount("/js", StaticFiles(directory=js_dir), name="js")
    print(f"JS mounted from: {js_dir}")


# ── Routes ─────────────────────────────────

@app.get("/")
def serve_frontend():
    """Serve the frontend dashboard."""
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"status": "online", "version": settings.APP_VERSION}


@app.get("/api/health")
def api_health():
    return {
        "status": "healthy",
        "models_loaded": False,
        "database_connected": True
    }


@app.get("/api/dashboard/summary")
def get_dashboard_summary():
    return {
        "income": 150000,
        "expenses": 95000,
        "savings": 55000,
        "savingsRate": 36.7
    }


@app.get("/api/dashboard/trends")
def get_trends():
    return {
        "months": ["Jan","Feb","Mar","Apr","May","Jun",
                   "Jul","Aug","Sep","Oct","Nov","Dec"],
        "income": [150000,152000,151000,150500,151500,150000,
                   150800,151200,150900,151100,150500,151000],
        "expenses": [80000,85000,82000,90000,95000,88000,
                     92000,105000,90000,95000,89000,92000]
    }


@app.get("/api/dashboard/categories")
def get_categories():
    return {
        "labels": ["Housing","Food","Transport",
                   "Entertainment","Shopping","Utilities"],
        "data": [30000,25000,15000,10000,10000,5000]
    }


@app.post("/api/predict/expenses")
def predict_expenses(data: dict = None):
    return {
        "months": ["Jan","Feb","Mar"],
        "predictedExpenses": [93000,94500,91000],
        "lowerBound": [90000,90000,85000],
        "upperBound": [96000,99000,97000]
    }


@app.post("/api/predict/forecast")
def forecast(data: dict = None):
    months = data.get("months", 3) if data else 3
    return {
        "months": ["Jan","Feb","Mar"][:months],
        "predictedExpenses": [93000,94500,91000][:months],
        "lowerBound": [90000,90000,85000][:months],
        "upperBound": [96000,99000,97000][:months]
    }


@app.post("/api/optimize/budget")
def optimize_budget(data: dict = None):
    return [
        {
            "priority": "high",
            "category": "Food",
            "current": 25000,
            "suggested": 20000,
            "savings": 5000,
            "message": "Cooking at home could save Rs.5,000."
        },
        {
            "priority": "medium",
            "category": "Entertainment",
            "current": 10000,
            "suggested": 7000,
            "savings": 3000,
            "message": "Cancel unused subscriptions to save Rs.3,000."
        },
        {
            "priority": "low",
            "category": "Transport",
            "current": 15000,
            "suggested": 13000,
            "savings": 2000,
            "message": "Optimizing commute could save Rs.2,000."
        }
    ]


@app.post("/api/optimize/savings-goal")
def analyze_savings_goal(data: dict = None):
    return {
        "feasible": True,
        "requiredMonthly": 29166,
        "message": "Based on current trajectory you will reach this goal on time."
    }


@app.get("/api/optimize/category-analysis")
def get_category_analysis():
    return {
        "categories": [
            {"name": "Housing",   "allocation": 50, "actual": 52},
            {"name": "Food",      "allocation": 15, "actual": 18},
            {"name": "Transport", "allocation": 10, "actual": 9}
        ]
    }


@app.get("/api/data/status")
def get_data_status():
    return {
        "status": "synced",
        "lastUpdate": "2024-01-15",
        "recordCount": 60
    }


@app.post("/api/data/generate")
def generate_data(data: dict = None):
    return {"success": True, "message": "Data generated successfully"}


@app.post("/api/data/train")
def train_models(data: dict = None):
    return {"success": True, "message": "Models trained successfully"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)