import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Risk Dashboard",
    page_icon="⚠️",
    layout="wide"
)

# ============================================================
# Paths
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

RISK_PATH = ROOT_DIR / "data" / "processed" / "risk_scoring.parquet"

SUMMARY_PATH = ROOT_DIR / "outputs" / "decision_summary.csv"

# ============================================================
# Load Data
# ============================================================

@st.cache_data
def load_data():
    risk = pd.read_parquet(RISK_PATH)
    summary = pd.read_csv(SUMMARY_PATH)
    return risk, summary

risk_df, summary_df = load_data()

# ============================================================
# Header
# ============================================================

st.title("⚠️ Inventory Risk Dashboard")

st.caption("Stockout & Overstock Decision Support System")

st.divider()

# ============================================================
# KPIs
# ============================================================

stockout = (risk_df["risk"] == "Stockout Risk").sum()

overstock = (risk_df["risk"] == "Overstock Risk").sum()

healthy = (risk_df["risk"] == "Healthy").sum()

sales_risk = risk_df["sales_at_risk_rs"].sum()

locked = risk_df["locked_capital_rs"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Stockout Risk",
    f"{stockout:,}"
)

c2.metric(
    "Overstock Risk",
    f"{overstock:,}"
)

c3.metric(
    "Sales at Risk",
    f"₹{sales_risk:,.0f}"
)

c4.metric(
    "Locked Capital",
    f"₹{locked:,.0f}"
)

st.divider()

# ============================================================
# Charts
# ============================================================

left, right = st.columns(2)

risk_count = (
    risk_df["risk"]
    .value_counts()
    .reset_index()
)

risk_count.columns = ["Risk", "Count"]

fig = px.pie(
    risk_count,
    names="Risk",
    values="Count",
    hole=0.55,
    title="Risk Distribution"
)

left.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    summary_df,
    x="risk",
    y="sku_count",
    color="priority",
    text="sku_count",
    title="SKU Count by Risk"
)

right.plotly_chart(fig, use_container_width=True)

st.divider()

# ============================================================
# Financial Impact
# ============================================================

impact = pd.DataFrame({
    "Metric": [
        "Sales at Risk",
        "Locked Capital"
    ],
    "Amount": [
        sales_risk,
        locked
    ]
})

fig = px.bar(
    impact,
    x="Metric",
    y="Amount",
    text="Amount",
    color="Metric",
    title="Estimated Financial Impact (₹)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# High Priority SKUs
# ============================================================

st.subheader("🚨 High Priority SKUs")

high = (
    risk_df[
        risk_df["risk"] == "Stockout Risk"
    ]
    .sort_values(
        "sales_at_risk_rs",
        ascending=False
    )
)

st.dataframe(
    high[
        [
            "item_id",
            "store_id",
            "rf_forecast",
            "sales_at_risk_rs",
            "recommended_action"
        ]
    ].head(100),
    use_container_width=True,
    height=400
)

# ============================================================
# Decision Grid
# ============================================================

st.subheader("Decision Grid")

st.dataframe(
    summary_df,
    use_container_width=True
)

st.divider()

# ============================================================
# Executive Insights
# ============================================================

st.subheader("Business Recommendations")

st.success(f"""
### Executive Summary

• Total Stockout Risks: **{stockout:,}**

• Total Overstock Risks: **{overstock:,}**

• Estimated Revenue at Risk: **₹{sales_risk:,.0f}**

• Estimated Locked Capital: **₹{locked:,.0f}**

### Recommended Actions

🔴 **High Priority**
- Replenish stock immediately.
- Increase inventory allocation.
- Monitor demand weekly.

🟠 **Medium Priority**
- Slow future purchasing.
- Launch promotions or markdowns.
- Rebalance inventory across stores.

🟢 **Low Priority**
- Maintain current inventory policy.
- Continue weekly monitoring.

The rule-based risk engine ensures every recommendation is transparent and directly traceable to the forecast outputs, satisfying the Project FORESIGHT client requirement for explainable inventory decision support.
""")
