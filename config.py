"""
Application configuration settings for the Personal Finance Prediction API.
"""

import os
from pathlib import Path


class Settings:
    """Central configuration for paths, CORS, and API metadata."""

    PROJECT_ROOT = Path(__file__).parent.parent.parent
    DATA_DIR = PROJECT_ROOT / "data" / "raw"
    DATA_PATH = DATA_DIR / "monthly_finance_data.csv"
    MODEL_DIR = Path(__file__).parent / "ml" / "artifacts"

    API_PREFIX = "/api"
    CORS_ORIGINS = ["*"]

    APP_TITLE = "Personal Finance Prediction API"
    APP_VERSION = "1.0.0"


settings = Settings()
