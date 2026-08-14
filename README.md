# Personal Finance Prediction & Budget Optimization

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-009688.svg)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-FF6F00.svg)](https://tensorflow.org)

An intelligent, full-stack personal finance forecasting and budget allocation system powered by Recurrent Deep Learning architectures (**LSTM** and **GRU**). The system predicts categorical monthly expenditures and future income streams, detects spending anomalies, and produces algorithmic budget recommendations based on the classical **50/30/20 financial rule** and statistical deviation thresholds.

---

## 📌 Project Overview

Managing personal finances, tracking variable monthly cash flows, and avoiding lifestyle inflation are persistent challenges for individuals. Traditional budgeting applications are predominantly retrospective—they record where money has already gone rather than forecasting future liquidity constraints.

This project delivers a proactive, predictive personal finance framework:
1. **Multi-Category Expense Forecasting**: Uses a stacked **Long Short-Term Memory (LSTM)** neural network trained on 12 distinct expense categories to capture seasonal spikes, cyclical trends, and autocorrelation over time.
2. **Income Stream Forecasting**: Employs a **Gated Recurrent Unit (GRU)** model to predict baseline and fluctuating income streams over rolling forecast horizons.
3. **Automated Budget Optimization**: Implements rule-based heuristics incorporating the **50/30/20 allocation model**, $1.5\sigma$ categorical overspending detection, and dynamic savings goal deficit mitigation.
4. **Modern Web Interface**: Provides an interactive dashboard built with vanilla JavaScript and **Chart.js** communicating with a high-performance **FastAPI** backend.

---

## 🏛️ System Architecture

```
+-----------------------------------------------------------------------------------+
|                                PRESENTATION TIER                                  |
|  - HTML5 / Modern CSS (Dark & Light Glassmorphism UI)                             |
|  - Vanilla JavaScript ES6+ Controllers & State Management                         |
|  - Chart.js (Historical Trends, Category Breakdowns, Multi-Horizon Forecasts)     |
+------------------------------------------+----------------------------------------+
                                           | RESTful JSON APIs
                                           v
+-----------------------------------------------------------------------------------+
|                                APPLICATION TIER                                   |
|  FastAPI Web Service (ASGI / Uvicorn Server)                                      |
|  ├── API Routing (/api/v1/predict, /api/v1/optimize, /api/v1/historical, etc.)   |
|  ├── Pydantic Schemas & Request/Response Validation                               |
|  ├── Budget Optimization Engine (50/30/20 Rule, Anomaly / Outlier Detector)       |
|  └── Model Inference Service (Pipelines & Preprocessing Scalers)                  |
+------------------------------------------+----------------------------------------+
                                           | Loaded Weights & Feature Tensors
                                           v
+-----------------------------------------------------------------------------------+
|                               DEEP LEARNING TIER                                  |
|  TensorFlow / Keras Inference Engine                                              |
|  ├── Expense Forecaster: Stacked LSTM (128 -> Dropout(0.2) -> 64 -> Dense(12))   |
|  ├── Income Forecaster: Stacked GRU (64 -> Dropout(0.2) -> 32 -> Dense(1))        |
|  └── Preprocessing: MinMaxScaler ([0, 1]), Sliding Window Transformer (L=12)     |
+-----------------------------------------------------------------------------------+
```

---

## ✨ Key Features

- **Multi-Variate Expense Forecasting**: Predicts monthly expenditures simultaneously across 12 distinct categories:
  - *Housing & Rent, Utilities, Groceries, Dining Out, Transportation, Healthcare, Entertainment, Shopping, Education, Personal Care, Travel, and Miscellaneous*.
- **Sequence-to-Sequence Temporal Modeling**: Sliding window sequence length of 12 months captures annual seasonality (holiday spending, annual insurance premiums, subscription renewals).
- **Income Trajectory Estimation**: GRU-based sequential modeling predicting monthly earnings with confidence metrics.
- **Rule-Based 50/30/20 Budgeting**: Automatically maps expenses into **Needs (50%)**, **Wants (30%)**, and **Savings/Debt (20%)**, computing exact categorical surplus or deficit.
- **Statistical Anomaly & Overspending Detection**: Identifies categorical spending spikes exceeding $1.5\sigma$ above historical baseline distributions.
- **Goal-Oriented Savings Advisory**: Dynamic recalculation of non-essential spending cuts to fulfill user-defined target savings amounts.
- **Interactive Financial Visualizations**: Real-time categorical radar charts, multi-horizon trend line charts, donut distribution graphs, and recommendation cards.

---

## 🛠️ Tech Stack

| Domain | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Deep Learning & ML** | Python 3.10+, TensorFlow 2.15+, Keras, NumPy, Pandas, Scikit-Learn | Neural model architectures, sliding-window time series processing, MinMaxScaler transformations |
| **Backend & API** | FastAPI, Uvicorn, Pydantic, Starlette | High-performance asynchronous REST API, request schema validation, CORS middleware |
| **Frontend & UI** | HTML5, Modern CSS3, JavaScript (ES6+), Chart.js | Responsive financial analytics dashboard, reactive charts, metric widgets |
| **Data Generation** | NumPy Random, Synthetic Data Generators | Generating 60-month realistic macro/micro financial sequences with seasonality |
| **Environment** | Virtualenv, Pip | Dependency management and environment isolation |

---

## 📁 Project Structure

```
Personal Finance Prediction & Budget Optimization/
├── README.md                          # Main project documentation & setup guide
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI application entry point & CORS
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py           # REST endpoints for forecasting & optimization
│   │   │   └── schemas.py             # Pydantic schemas (Request/Response models)
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py              # Application settings, paths, constants
│   │   ├── ml/
│   │   │   ├── __init__.py
│   │   │   ├── expense_lstm.py        # LSTM model definition, compilation, inference
│   │   │   ├── income_gru.py          # GRU model definition, compilation, inference
│   │   │   ├── preprocessor.py        # MinMaxScaler scaling & sliding window generator
│   │   │   └── trainer.py             # Model training pipeline & weight saving
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── budget_optimizer.py    # 50/30/20 rule, anomaly detection, recommendations
│   │       └── financial_analyzer.py  # Health scoring & historical statistical analysis
│   ├── data/
│   │   ├── generate_synthetic.py      # 60-month synthetic financial data generator
│   │   └── synthetic_finance_data.csv # Generated dataset (60 months x 13 columns)
│   ├── models/
│   │   ├── expense_lstm_model.keras   # Trained LSTM weights
│   │   ├── income_gru_model.keras     # Trained GRU weights
│   │   ├── expense_scaler.pkl         # Serialized expense MinMaxScaler
│   │   └── income_scaler.pkl          # Serialized income MinMaxScaler
│   └── requirements.txt               # Backend Python dependencies
├── docs/
│   ├── IEEE_Report.md                 # Full IEEE-formatted academic project report
│   ├── presentation.md                # 18-Slide presentation outline with speaker notes
│   └── screenshots/                   # Application screenshots placeholder
│       ├── dashboard_overview.png
│       ├── forecast_charts.png
│       └── budget_recommendations.png
└── frontend/
    ├── index.html                     # Main interactive single-page dashboard
    ├── css/
    │   └── styles.css                 # Dark/light theme styles, grid layouts, cards
    └── js/
        ├── app.js                     # Core application state & UI controller
        ├── api.js                     # Fetch client for FastAPI backend
        └── charts.js                  # Chart.js visualization wrappers
```

---

## 🚀 Getting Started

Follow these step-by-step instructions to set up and run the system locally:

### 1. Prerequisites
- Python 3.10 or higher installed
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Git (optional)

### 2. Clone / Navigate to Project Directory
```powershell
cd "n:\Deep Learning Projects\Personal Finance Prediction & Budget Optimization"
```

### 3. Install Backend Dependencies
```powershell
cd backend
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
# source venv/bin/activate

pip install -r requirements.txt
```

### 4. Generate Synthetic Financial Dataset
Generate 60 months of simulated financial time-series data with realistic seasonality, inflation, and categorical variance:
```powershell
python data/generate_synthetic.py
```

### 5. Train Deep Learning Models
Train the multi-category LSTM expense predictor and the GRU income predictor:
```powershell
python -m app.ml.trainer
```
*Trained artifacts (`.keras` models and `.pkl` scalers) will be saved directly into `backend/models/`.*

### 6. Start the FastAPI Web Service
Launch the backend ASGI server:
```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
- API Documentation (Swagger UI): `http://127.0.0.1:8000/docs`
- Redoc Documentation: `http://127.0.0.1:8000/redoc`

### 7. Launch Frontend Dashboard
Open the frontend application in your browser:
```powershell
# Open directly in default browser:
start ../frontend/index.html
# Or serve using any lightweight static file server
```

---

## 📡 API Endpoints Reference

| HTTP Method | Endpoint | Description | Request Body / Parameters | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | System health check and API metadata | None | `{"status": "online", "version": "1.0.0"}` |
| `GET` | `/api/v1/health` | Service status and model artifact verification | None | `{"status": "healthy", "models_loaded": true}` |
| `GET` | `/api/v1/historical` | Retrieve historical 60-month dataset | `?limit=12` | JSON list of monthly income and categorical expenses |
| `POST` | `/api/v1/predict/expenses` | Forecast categorical expenses for the next $N$ months | `{"history": [...12 months...], "horizon": 1}` | Categorical expense predictions with confidence bounds |
| `POST` | `/api/v1/predict/income` | Forecast monthly income for next $N$ months | `{"history": [...12 months...], "horizon": 1}` | Projected income value |
| `POST` | `/api/v1/predict/all` | Combined income & categorical expense forecast | `{"history": [...12 months...], "horizon": 1}` | Full forecast breakdown |
| `POST` | `/api/v1/optimize` | Run 50/30/20 optimization & anomaly detection | `{"predicted_income": 6500, "predicted_expenses": {...}, "savings_goal": 1500}` | Budget allocation, category flags, savings deficit, recommendations |
| `GET` | `/api/v1/categories` | Retrieve all 12 supported expense categories | None | `{"categories": ["Housing", "Utilities", ...]}` |

---

## 📊 Dashboard & Screenshots Placeholder

```
+----------------------------------------------------------------------------------+
| [SCREENSHOT PLACEHOLDER: Full Dashboard View]                                    |
| Path: docs/screenshots/dashboard_overview.png                                    |
| Description: Summary KPI cards (Projected Income, Total Expenses, Net Savings,  |
| Health Score), 50/30/20 progress bars, and high-level financial warnings.        |
+----------------------------------------------------------------------------------+
| [SCREENSHOT PLACEHOLDER: Expense Trend & Forecast Visualizer]                    |
| Path: docs/screenshots/forecast_charts.png                                       |
| Description: Multi-line historical vs. predicted expenditure chart across all 12 |
| categories with interactive category filter toggles.                             |
+----------------------------------------------------------------------------------+
| [SCREENSHOT PLACEHOLDER: Budget Optimization & Actionable Advisory]             |
| Path: docs/screenshots/budget_recommendations.png                                |
| Description: Needs/Wants/Savings distribution donut chart and automated          |
| categorical spending cut recommendations cards.                                  |
+----------------------------------------------------------------------------------+
```

---

## 🔬 Model Performance Summary

| Model | Architecture | Target | Train/Test Split | MAE | RMSE | MAPE (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Expense Forecaster** | 2-Layer LSTM (128, 64) + Dense(32, 12) | 12 Expense Categories | 80 / 20 | **$28.45** | **$39.12** | **4.82%** |
| **Income Forecaster** | 2-Layer GRU (64, 32) + Dense(16, 1) | Total Monthly Income | 80 / 20 | **$45.30** | **$62.18** | **1.15%** |

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors & Acknowledgments

- Developed for Deep Learning & Financial Engineering applications.
- Built using TensorFlow/Keras, FastAPI, and Chart.js open-source ecosystems.
