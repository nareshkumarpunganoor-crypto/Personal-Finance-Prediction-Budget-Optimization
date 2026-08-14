# Quick Start Guide - Personal Finance Prediction & Budget Optimization

## ✅ Application Status

The **Frontend** has been launched successfully and is now open in your browser at:
- **File Location**: `frontend/index.html`

The frontend dashboard includes:
- 📊 Summary Cards (Income, Expenses, Savings)
- 📈 Financial Trends Charts
- 🎯 Category Breakdown Analysis
- 💰 Budget Optimization Recommendations
- 🔮 Expense Forecasting
- ⚙️ Interactive Controls

---

## 🔧 Backend Setup (If Needed)

The frontend can work in **offline mode** with fallback mock data, or you can set up the backend API for real predictions.

### Prerequisites
- Python 3.10 or higher
- Virtual Environment (recommended)

### Step 1: Install Dependencies

Navigate to the backend directory:
```powershell
cd backend
```

Create and activate a virtual environment:
```powershell
# Create virtual environment
python -m venv venv

# Activate on Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Or on Windows CMD:
venv\Scripts\activate.bat
```

Install required packages (skip TensorFlow for Python 3.14):
```powershell
pip install fastapi pydantic uvicorn python-multipart pandas numpy scikit-learn
```

### Step 2: Start the Backend Server

From the `backend` directory with virtual environment activated:
```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Step 3: Access the API Documentation

Open your browser to:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 🌐 Frontend Features

### Available Endpoints (Mocked in Offline Mode)

1. **Dashboard Summary** - Income, Expenses, Savings metrics
2. **Financial Trends** - 12-month historical data visualization
3. **Category Analysis** - Expense breakdown by category
4. **Expense Forecasting** - 3-month predictions
5. **Budget Optimization** - AI-powered recommendations
6. **Savings Goal Analysis** - Goal feasibility assessment

### Theme Toggle
Click the theme icon in the top-right corner to switch between:
- 🌙 Dark Mode (Glassmorphism)
- ☀️ Light Mode

### Responsive Design
The dashboard is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile devices

---

## 📂 Project Structure

```
Personal Finance Prediction & Budget Optimization/
├── frontend/
│   ├── index.html          # Main dashboard (now open in browser)
│   ├── css/styles.css      # Styling & themes
│   └── js/
│       ├── app.js          # Application logic
│       ├── api.js          # API client with fallback data
│       └── charts.js       # Chart visualizations
│
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI application (created)
│   │   ├── config.py       # Configuration settings
│   │   ├── api/            # API routes
│   │   ├── ml/             # Machine learning models
│   │   └── services/       # Business logic
│   ├── data/
│   │   └── generate_synthetic.py  # Data generator
│   └── requirements.txt    # Dependencies
│
└── docs/
    ├── IEEE_Report.md      # Full technical documentation
    └── presentation.md     # Presentation slides
```

---

## 💡 Features Overview

### ✨ AI-Powered Analysis
- **LSTM Neural Network** for expense forecasting
- **GRU Model** for income prediction
- **Anomaly Detection** for unusual spending
- **50/30/20 Budget Rule** implementation

### 📊 Interactive Visualizations
- Line charts for trends
- Pie charts for category breakdown
- Radar charts for budget allocation
- Donut charts for expense distribution

### 🎯 Smart Recommendations
- Automated budget optimization
- Savings goal tracking
- Spending anomaly alerts
- Category-based insights

---

## 🐛 Troubleshooting

### Issue: "Connecting..." Status Never Changes
**Solution**: This is normal in offline mode. The frontend uses mock data for all API calls.

### Issue: Backend Port 8000 Already in Use
**Solution**: Change the port:
```powershell
python -m uvicorn app.main:app --port 8001
```

Then update `api.js` to use the new port.

### Issue: Module Not Found Errors
**Solution**: Make sure you've installed all dependencies:
```powershell
pip install -r requirements.txt
```

---

## 📚 Documentation

For detailed technical documentation, see:
- **IEEE Report**: `docs/IEEE_Report.md`
- **Presentation**: `docs/presentation.md`

---

## ✅ What's Ready

- ✅ Frontend Dashboard (Open in Browser)
- ✅ API Structure (Created)
- ✅ Mock Data (Available)
- ✅ CSS Styling (Dark/Light Themes)
- ✅ JavaScript Interactivity

---

## 🚀 Next Steps

1. **Explore the Dashboard**: Navigate through all sections and features
2. **(Optional) Set Up Backend**: Follow the Backend Setup steps to connect real APIs
3. **(Optional) Train Models**: Run model training scripts for ML predictions
4. **(Optional) Generate Data**: Create synthetic financial datasets

---

**Enjoy your Personal Finance Dashboard! 🎉**
