"""
Synthetic Personal Finance Data Generator
==========================================

Generates 5 years (Jan 2020 - Dec 2024) of realistic monthly personal finance
data for an Indian household. Includes salary with annual raises, festival
bonuses, seasonal spending patterns, and gradual inflation on variable expenses.

Output: backend/data/raw/monthly_finance_data.csv
"""

import os
from typing import Tuple

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SEED: int = 42
START_YEAR: int = 2020
END_YEAR: int = 2024
BASE_SALARY: float = 50_000.0  # ₹50,000/month
ANNUAL_RAISE_RANGE: Tuple[float, float] = (0.05, 0.08)  # 5-8 %
BONUS_MONTHS: Tuple[int, int] = (6, 12)  # June & December
BONUS_MULTIPLIER_RANGE: Tuple[float, float] = (0.50, 1.00)
ANNUAL_INFLATION: float = 0.03  # 3 % on variable expenses

# Expense definitions: (base, std_dev, is_fixed)
EXPENSE_CATEGORIES: dict = {
    "rent":          (12_000, 500,   True),
    "utilities":     (3_000,  800,   True),
    "insurance":     (2_000,  200,   True),
    "subscriptions": (1_500,  300,   True),
    "emi":           (5_000,  0,     True),
    "food":          (8_000,  2_000, False),
    "transport":     (4_000,  1_500, False),
    "entertainment": (3_000,  1_500, False),
    "shopping":      (5_000,  3_000, False),
    "healthcare":    (2_000,  1_000, False),
    "education":     (3_000,  1_000, False),
    "personal_care": (1_500,  500,   False),
}

# Seasonal multipliers by month (1-indexed → index 0 unused)
# Higher entertainment/shopping in Oct-Dec (Diwali/Christmas)
# Higher transport in May-Jun (summer travel)
SEASONAL_MULTIPLIERS: dict = {
    "entertainment": {10: 1.5, 11: 1.8, 12: 1.6},
    "shopping":      {10: 1.6, 11: 2.0, 12: 1.7},
    "transport":     {5: 1.4, 6: 1.5},
}


def _compute_income(
    month_index: int,
    month: int,
    rng: np.random.RandomState,
) -> float:
    """Compute monthly income including salary growth and bonuses.

    Parameters
    ----------
    month_index : int
        0-based index across the 60-month span (used for annual raises).
    month : int
        Calendar month (1-12).
    rng : np.random.RandomState
        Seeded random-state instance.

    Returns
    -------
    float
        Total income for the month in ₹.
    """
    years_elapsed = month_index // 12
    # Deterministic raise per year (drawn once per year from the range)
    cumulative_raise = 1.0
    for y in range(years_elapsed):
        raise_pct = rng.uniform(*ANNUAL_RAISE_RANGE)
        cumulative_raise *= (1.0 + raise_pct)

    salary = BASE_SALARY * cumulative_raise

    bonus = 0.0
    if month in BONUS_MONTHS:
        bonus = salary * rng.uniform(*BONUS_MULTIPLIER_RANGE)

    return round(salary + bonus, 2)


def _compute_expense(
    category: str,
    base: float,
    std: float,
    is_fixed: bool,
    month: int,
    month_index: int,
    rng: np.random.RandomState,
) -> float:
    """Compute a single expense category value for one month.

    Parameters
    ----------
    category : str
        Expense category name.
    base : float
        Base monthly amount in ₹.
    std : float
        Standard deviation for random variation.
    is_fixed : bool
        Whether the category is a fixed expense (no inflation).
    month : int
        Calendar month (1-12).
    month_index : int
        0-based index across the 60-month span.
    rng : np.random.RandomState
        Seeded random-state instance.

    Returns
    -------
    float
        Expense amount in ₹ (non-negative).
    """
    # Apply inflation to variable expenses only
    inflation_factor = 1.0
    if not is_fixed:
        years_elapsed = month_index / 12.0
        inflation_factor = (1.0 + ANNUAL_INFLATION) ** years_elapsed

    amount = rng.normal(base * inflation_factor, std)

    # Seasonal boost
    if category in SEASONAL_MULTIPLIERS:
        multiplier = SEASONAL_MULTIPLIERS[category].get(month, 1.0)
        amount *= multiplier

    return round(max(amount, 0.0), 2)


def generate_finance_data(seed: int = SEED) -> pd.DataFrame:
    """Generate 60 months of synthetic personal finance data.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: year, month, income, 12 expense categories,
        total_expenses, savings.
    """
    rng = np.random.RandomState(seed)
    records: list = []

    month_index = 0
    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            income = _compute_income(month_index, month, rng)

            expenses: dict = {}
            for cat, (base, std, is_fixed) in EXPENSE_CATEGORIES.items():
                expenses[cat] = _compute_expense(
                    cat, base, std, is_fixed, month, month_index, rng,
                )

            total_expenses = round(sum(expenses.values()), 2)
            savings = round(income - total_expenses, 2)

            record = {
                "year": year,
                "month": month,
                "income": income,
                **expenses,
                "total_expenses": total_expenses,
                "savings": savings,
            }
            records.append(record)
            month_index += 1

    return pd.DataFrame(records)


def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Save the generated DataFrame to CSV.

    Parameters
    ----------
    df : pd.DataFrame
        Finance data.
    output_path : str
        Destination CSV path.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Saved {len(df)} records to {output_path}")


# ---------------------------------------------------------------------------
# Entry-point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    OUTPUT_PATH = os.path.join(
        os.path.dirname(__file__), "raw", "monthly_finance_data.csv"
    )

    data = generate_finance_data()
    save_data(data, OUTPUT_PATH)

    # Quick summary
    print(f"\n{'='*60}")
    print("Personal Finance Data — Summary (₹)")
    print(f"{'='*60}")
    print(f"  Months generated : {len(data)}")
    print(f"  Date range       : {data['year'].min()}-01 → {data['year'].max()}-12")
    print(f"  Avg. Income      : ₹{data['income'].mean():,.2f}")
    print(f"  Avg. Expenses    : ₹{data['total_expenses'].mean():,.2f}")
    print(f"  Avg. Savings     : ₹{data['savings'].mean():,.2f}")
    print(f"{'='*60}")
    print(data.head(6).to_string(index=False))
