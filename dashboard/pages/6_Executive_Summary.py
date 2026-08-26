import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Executive Summary",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# Paths
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

FORECAST_PATH = ROOT_DIR / "data" / "processed" / "weekly_forecasts.parquet"
RISK_PATH = ROOT_DIR / "data" / "processed" / "risk_scoring.parquet"
SUMMARY_PATH = ROOT_DIR / "outputs" / "decision_summary.csv"

# ============================================================
# Load Data
# ============================================================

@st.cache_data
def load_data():

    forecast = pd.read_parquet(FORECAST_PATH)

    risk = pd.read_parquet(RISK_PATH)

    summary = pd.read_csv(SUMMARY_PATH)

    return forecast, risk, summary


forecast_df, risk_df, summary_df = load_data()

# ============================================================
# KPIs
# ============================================================

baseline_wape = 0.7141
rf_wape = 0.5905

improvement = (
    (baseline_wape - rf_wape)
    / baseline_wape
) * 100

total_units = int(forecast_df["units_sold"].sum())

forecast_units = int(forecast_df["rf_forecast"].sum())

sales_risk = risk_df["sales_at_risk_rs"].sum()

locked_capital = risk_df["locked_capital_rs"].sum()

stockout = (risk_df["risk"] == "Stockout Risk").sum()

overstock = (risk_df["risk"] == "Overstock Risk").sum()

healthy = (risk_df["risk"] == "Healthy").sum()

# ============================================================
# Header
# ============================================================

st.title("📊 Executive Summary")

st.caption(
    "Project FORESIGHT • Retail Demand Forecasting & Inventory Risk Analytics"
)

st.divider()

# ============================================================
# Executive KPI Cards
# ============================================================

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Total Units Sold",
    f"{total_units:,}"
)

k2.metric(
    "Forecast Units",
    f"{forecast_units:,}"
)

k3.metric(
    "Random Forest WAPE",
    f"{rf_wape:.4f}"
)

k4.metric(
    "Accuracy Improvement",
    f"{improvement:.1f}%"
)

st.divider()

# ============================================================
# Operational KPI Cards
# ============================================================

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Healthy SKUs",
    f"{healthy:,}"
)

k2.metric(
    "Stockout Risks",
    f"{stockout:,}"
)

k3.metric(
    "Overstock Risks",
    f"{overstock:,}"
)

k4.metric(
    "Sales at Risk",
    f"₹{sales_risk:,.0f}"
)

st.divider()

# ============================================================
# Charts
# ============================================================

left, right = st.columns(2)

# Risk Distribution

risk_counts = (
    risk_df["risk"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = ["Risk", "Count"]

fig = px.pie(
    risk_counts,
    names="Risk",
    values="Count",
    hole=0.60,
    title="Inventory Risk Distribution"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# Model Performance

performance = pd.DataFrame(
    {
        "Model": [
            "Seasonal Naive",
            "Random Forest"
        ],
        "WAPE": [
            baseline_wape,
            rf_wape
        ]
    }
)

fig = px.bar(
    performance,
    x="Model",
    y="WAPE",
    color="Model",
    text="WAPE",
    title="Forecast Model Performance"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# Financial Impact
# ============================================================

impact = pd.DataFrame(
    {
        "Category": [
            "Sales at Risk",
            "Locked Capital"
        ],
        "Amount": [
            sales_risk,
            locked_capital
        ]
    }
)

fig = px.bar(
    impact,
    x="Category",
    y="Amount",
    text="Amount",
    color="Category",
    title="Estimated Financial Impact (₹)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ============================================================
# Decision Summary
# ============================================================

st.subheader("Decision Summary")

st.dataframe(
    summary_df,
    use_container_width=True
)

st.divider()

# ============================================================
# Project Deliverables
# ============================================================

st.subheader("Project Deliverables")

deliverables = pd.DataFrame({

    "Deliverable":[
        "Data Pipeline",
        "EDA & Insights",
        "Demand Forecasting",
        "Risk Scoring",
        "Interactive Dashboard",
        "Deployment Ready"
    ],

    "Status":[
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Ready"
    ]

})

st.dataframe(
    deliverables,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ============================================================
# Executive Recommendations
# ============================================================

st.subheader("Executive Recommendations")

st.success(f"""

### Key Business Findings

• Total Units Analysed: **{total_units:,}**

• Random Forest reduced forecasting error from **{baseline_wape:.4f}** to **{rf_wape:.4f}**, an improvement of **{improvement:.1f}%**.

• **{stockout:,}** SKU-weeks are at stockout risk, representing approximately **₹{sales_risk:,.0f}** in potential sales exposure.

• **{overstock:,}** SKU-weeks are overstocked, tying up approximately **₹{locked_capital:,.0f}** in working capital.

### Recommended Actions

🔴 **High Priority**
- Replenish stock for high-demand SKUs immediately.
- Increase monitoring of fast-moving products.

🟠 **Medium Priority**
- Reduce purchasing for overstocked items.
- Use promotions or markdown campaigns to improve inventory turnover.

🟢 **Low Priority**
- Maintain current replenishment strategy for healthy inventory.
- Continue weekly forecast monitoring.

### Overall Outcome

Project FORESIGHT successfully delivers a reproducible forecasting pipeline, a backtested machine learning model that outperforms the seasonal-naive baseline, transparent inventory risk scoring, and interactive dashboards that support operational and executive decision-making.

""")
