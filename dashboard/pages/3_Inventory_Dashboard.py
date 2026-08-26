import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Inventory Dashboard",
    page_icon="📦",
    layout="wide"
)

# ============================================================
# Paths
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

FORECAST_PATH = ROOT_DIR / "data" / "processed" / "weekly_forecasts.parquet"
RISK_PATH = ROOT_DIR / "data" / "processed" / "risk_scoring.parquet"

# ============================================================
# Load Data
# ============================================================

@st.cache_data
def load_data():
    forecast = pd.read_parquet(FORECAST_PATH)
    risk = pd.read_parquet(RISK_PATH)
    return forecast, risk

forecast_df, risk_df = load_data()

# ============================================================
# Merge
# ============================================================

df = forecast_df.merge(
    risk_df[
        [
            "item_id",
            "store_id",
            "year",
            "week_of_year",
            "risk",
            "recommended_action",
            "sales_at_risk_rs",
            "locked_capital_rs"
        ]
    ],
    on=["item_id","store_id","year","week_of_year"],
    how="left"
)

# ============================================================
# Sidebar
# ============================================================

st.sidebar.header("Inventory Filters")

stores = sorted(df.store_id.unique())

selected_store = st.sidebar.multiselect(
    "Store",
    stores,
    default=stores
)

df = df[df.store_id.isin(selected_store)]

# ============================================================
# Header
# ============================================================

st.title("📦 Inventory Dashboard")

st.caption("Inventory Planning & Replenishment Monitoring")

st.divider()

# ============================================================
# KPIs
# ============================================================

stockout = (df.risk=="Stockout Risk").sum()

overstock = (df.risk=="Overstock Risk").sum()

healthy = (df.risk=="Healthy").sum()

capital = df.locked_capital_rs.sum()

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Healthy SKUs",
    f"{healthy:,}"
)

c2.metric(
    "Stockout Risks",
    f"{stockout:,}"
)

c3.metric(
    "Overstock Risks",
    f"{overstock:,}"
)

c4.metric(
    "Locked Capital",
    f"₹{capital:,.0f}"
)

st.divider()

# ============================================================
# Inventory Status
# ============================================================

left,right = st.columns(2)

risk_count = (
    df["risk"]
    .value_counts()
    .reset_index()
)

risk_count.columns = ["Risk","Count"]

fig = px.pie(
    risk_count,
    names="Risk",
    values="Count",
    hole=.55,
    title="Inventory Status"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

store_inventory = (
    df.groupby("store_id")["units_sold"]
    .sum()
    .reset_index()
)

fig = px.bar(
    store_inventory,
    x="store_id",
    y="units_sold",
    title="Demand by Store"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# Top Reorder List
# ============================================================

st.subheader("🚨 Immediate Reorder Recommendations")

reorder = (
    df[df.risk=="Stockout Risk"]
    .sort_values(
        "sales_at_risk_rs",
        ascending=False
    )
)

st.dataframe(
    reorder[
        [
            "item_id",
            "store_id",
            "rf_forecast",
            "sales_at_risk_rs",
            "recommended_action"
        ]
    ].head(50),
    use_container_width=True,
    height=400
)

# ============================================================
# Overstock List
# ============================================================

st.subheader("📉 Overstock Monitoring")

over = (
    df[df.risk=="Overstock Risk"]
    .sort_values(
        "locked_capital_rs",
        ascending=False
    )
)

st.dataframe(
    over[
        [
            "item_id",
            "store_id",
            "locked_capital_rs",
            "recommended_action"
        ]
    ].head(50),
    use_container_width=True,
    height=400
)

# ============================================================
# Executive Summary
# ============================================================

st.subheader("Business Summary")

st.success(f"""

### Inventory Health Overview

✅ Healthy SKUs : **{healthy:,}**

⚠️ Stockout Risks : **{stockout:,}**

📦 Overstock Risks : **{overstock:,}**

💰 Locked Capital : **₹{capital:,.0f}**

The dashboard prioritizes SKUs requiring immediate replenishment while identifying products contributing to excess inventory carrying costs.

Recommended actions are generated directly from the risk scoring engine developed in Notebook 05.
""")
