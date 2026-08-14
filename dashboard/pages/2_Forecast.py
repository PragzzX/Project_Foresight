import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="Forecast Dashboard",
    page_icon="🔮",
    layout="wide"
)

# ============================================================
# Paths
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT_DIR / "data" / "processed" / "weekly_forecasts.parquet"

# ============================================================
# Load Data
# ============================================================

@st.cache_data
def load_data():
    return pd.read_parquet(DATA_PATH)

df = load_data()

# ============================================================
# Sidebar Filters
# ============================================================

st.sidebar.header("Forecast Filters")

stores = sorted(df.store_id.unique())

selected_store = st.sidebar.multiselect(
    "Store",
    stores,
    default=stores
)

years = sorted(df.year.unique())

selected_year = st.sidebar.multiselect(
    "Year",
    years,
    default=years
)

df = df[
    (df.store_id.isin(selected_store))
    &
    (df.year.isin(selected_year))
]

# ============================================================
# Header
# ============================================================

st.title("🔮 Demand Forecast Dashboard")

st.caption("AI-based Weekly SKU Demand Forecasting")

st.divider()

# ============================================================
# Metrics
# ============================================================

forecast_total = int(df.rf_forecast.sum())

baseline_total = int(df.baseline_forecast.sum())

actual_total = int(df.units_sold.sum())

baseline_wape = 0.7141
rf_wape = 0.5905

improvement = (
    (baseline_wape-rf_wape)
    /
    baseline_wape
)*100

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Forecast Units",
    f"{forecast_total:,}"
)

c2.metric(
    "Actual Units",
    f"{actual_total:,}"
)

c3.metric(
    "Random Forest WAPE",
    f"{rf_wape:.3f}"
)

c4.metric(
    "Improvement",
    f"{improvement:.1f}%"
)

st.divider()

# ============================================================
# Weekly Forecast Trend
# ============================================================

weekly = (
    df.groupby(
        ["year","week_of_year"],
        as_index=False
    )[
        [
            "units_sold",
            "baseline_forecast",
            "rf_forecast"
        ]
    ]
    .sum()
)

weekly["Week"] = (
    weekly.year.astype(str)
    + "-W"
    + weekly.week_of_year.astype(str)
)

fig = px.line(
    weekly,
    x="Week",
    y=[
        "units_sold",
        "baseline_forecast",
        "rf_forecast"
    ],
    markers=True,
    title="Actual vs Forecast"
)

fig.update_layout(height=550)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ============================================================
# Distribution
# ============================================================

left,right = st.columns(2)

fig = px.histogram(
    df,
    x="rf_forecast",
    nbins=50,
    title="Forecast Distribution"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

comparison = pd.DataFrame({
    "Model":[
        "Seasonal Baseline",
        "Random Forest"
    ],
    "WAPE":[
        baseline_wape,
        rf_wape
    ]
})

fig = px.bar(
    comparison,
    x="Model",
    y="WAPE",
    text="WAPE",
    title="Model Performance"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# Forecast Table
# ============================================================

st.subheader("Forecast Results")

st.dataframe(
    df[
        [
            "item_id",
            "store_id",
            "year",
            "week_of_year",
            "units_sold",
            "baseline_forecast",
            "rf_forecast"
        ]
    ],
    use_container_width=True,
    height=450
)

# ============================================================
# Business Insights
# ============================================================

st.subheader("Executive Insights")

st.success(f"""
✅ Total Forecast Demand : **{forecast_total:,} units**

✅ Actual Weekly Demand : **{actual_total:,} units**

✅ Baseline WAPE : **{baseline_wape:.4f}**

✅ Random Forest WAPE : **{rf_wape:.4f}**

✅ Forecast Accuracy Improved by **{improvement:.1f}%** over the Seasonal Naive Baseline.

The Random Forest model captures temporal demand patterns more accurately, making it suitable for inventory planning and stock replenishment decisions.
""")