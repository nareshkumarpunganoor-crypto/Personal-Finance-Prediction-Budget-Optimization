"""
Main FastAPI application entry point for Personal Finance Prediction API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="Personal Finance Prediction & Budget Optimization API"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
def health_check():
    """API health check endpoint."""
    return {
        "status": "online",
        "version": settings.APP_VERSION,
        "app_title": settings.APP_TITLE
    }

@app.get("/api/health")
def api_health():
    """Detailed health check."""
    return {
        "status": "healthy",
        "models_loaded": False,  # Update based on actual model loading
        "database_connected": True
    }

# Basic example endpoints (expand with real implementations)
@app.get("/api/dashboard/summary")
def get_dashboard_summary():
    """Get dashboard summary data."""
    return {
        "income": 150000,
        "expenses": 95000,
        "savings": 55000,
        "savingsRate": 36.7
    }

@app.get("/api/dashboard/trends")
def get_trends():
    """Get financial trends."""
    return {
        "months": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        "income": [150000, 152000, 151000, 150500, 151500, 150000, 150800, 151200, 150900, 151100, 150500, 151000],
        "expenses": [80000, 85000, 82000, 90000, 95000, 88000, 92000, 105000, 90000, 95000, 89000, 92000]
    }

@app.get("/api/dashboard/categories")
def get_categories():
    """Get expense categories breakdown."""
    return {
        "labels": ['Housing', 'Food', 'Transport', 'Entertainment', 'Shopping', 'Utilities'],
        "data": [30000, 25000, 15000, 10000, 10000, 5000]
    }

@app.post("/api/predict/expenses")
def predict_expenses(data: dict = None):
    """Predict future expenses."""
    return {
        "months": ['Jan', 'Feb', 'Mar'],
        "predictedExpenses": [93000, 94500, 91000],
        "lowerBound": [90000, 90000, 85000],
        "upperBound": [96000, 99000, 97000]
    }

@app.post("/api/predict/forecast")
def forecast(data: dict = None):
    """Forecast expenses for specified months."""
    months = data.get('months', 3) if data else 3
    return {
        "months": ['Jan', 'Feb', 'Mar'][:months],
        "predictedExpenses": [93000, 94500, 91000][:months],
        "lowerBound": [90000, 90000, 85000][:months],
        "upperBound": [96000, 99000, 97000][:months]
    }

@app.post("/api/optimize/budget")
def optimize_budget(data: dict = None):
    """Get budget optimization recommendations."""
    return [
        {
            "priority": "high",
            "category": "Food",
            "current": 25000,
            "suggested": 20000,
            "savings": 5000,
            "message": "Dining out frequency has increased by 20% this month. Cooking at home could save ₹5,000."
        },
        {
            "priority": "medium",
            "category": "Entertainment",
            "current": 10000,
            "suggested": 7000,
            "savings": 3000,
            "message": "You have multiple unused subscriptions. Cancel them to save ₹3,000."
        },
        {
            "priority": "low",
            "category": "Transport",
            "current": 15000,
            "suggested": 13000,
            "savings": 2000,
            "message": "Optimizing your commute could save you ₹2,000."
        }
    ]

@app.post("/api/optimize/savings-goal")
def analyze_savings_goal(data: dict = None):
    """Analyze savings goal feasibility."""
    return {
        "feasible": True,
        "requiredMonthly": 29166,
        "message": "Based on current trajectory, you will reach this goal on time."
    }

@app.get("/api/optimize/category-analysis")
def get_category_analysis():
    """Get detailed category analysis."""
    return {
        "categories": [
            {"name": "Housing", "allocation": 50, "actual": 52},
            {"name": "Food", "allocation": 15, "actual": 18},
            {"name": "Transport", "allocation": 10, "actual": 9}
        ]
    }

@app.get("/api/data/status")
def get_data_status():
    """Get data synchronization status."""
    return {
        "status": "synced",
        "lastUpdate": "2024-01-15",
        "recordCount": 60
    }

@app.post("/api/data/generate")
def generate_data(data: dict = None):
    """Generate synthetic financial data."""
    return {"success": True, "message": "Data generated successfully"}

@app.post("/api/data/train")
def train_models(data: dict = None):
    """Train ML models."""
    return {"success": True, "message": "Models trained successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
