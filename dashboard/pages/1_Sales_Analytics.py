import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📈",
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
# Sidebar
# ============================================================

st.sidebar.header("Filters")

stores = sorted(df["store_id"].unique())

selected_store = st.sidebar.multiselect(
    "Store",
    stores,
    default=stores
)

years = sorted(df["year"].unique())

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

st.title("📈 Sales Analytics Dashboard")

st.caption("Interactive Retail Sales Performance Dashboard")

st.divider()

# ============================================================
# KPIs
# ============================================================

total_sales = int(df.units_sold.sum())

total_store = df.store_id.nunique()

total_sku = df.item_id.nunique()

avg_sales = round(df.units_sold.mean(),2)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Units Sold",
    f"{total_sales:,}"
)

c2.metric(
    "Stores",
    total_store
)

c3.metric(
    "Unique SKUs",
    total_sku
)

c4.metric(
    "Average Weekly Sales",
    avg_sales
)

st.divider()

# ============================================================
# Weekly Sales Trend
# ============================================================

weekly = (
    df.groupby(
        ["year","week_of_year"],
        as_index=False
    )["units_sold"]
    .sum()
)

weekly["Week"] = (
    weekly["year"].astype(str)
    + "-W"
    + weekly["week_of_year"].astype(str)
)

fig = px.line(
    weekly,
    x="Week",
    y="units_sold",
    markers=True,
    title="Weekly Sales Trend"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ============================================================
# Charts
# ============================================================

left,right = st.columns(2)

# Top Products

top_products = (
    df.groupby("item_id")["units_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="units_sold",
    y="item_id",
    orientation="h",
    title="Top 10 Selling Products"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# Store Sales

store_sales = (
    df.groupby("store_id")["units_sold"]
    .sum()
    .reset_index()
)

fig = px.pie(
    store_sales,
    names="store_id",
    values="units_sold",
    hole=.55,
    title="Store Contribution"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# Monthly Heatmap Table
# ============================================================

pivot = df.pivot_table(
    values="units_sold",
    index="store_id",
    columns="year",
    aggfunc="sum"
)

st.subheader("Store Sales Matrix")

st.dataframe(
    pivot,
    use_container_width=True
)

# ============================================================
# Business Insights
# ============================================================

st.subheader("Business Insights")

best_store = (
    store_sales
    .sort_values(
        "units_sold",
        ascending=False
    )
    .iloc[0]
)

best_product = (
    top_products.iloc[0]
)

st.success(f"""
• Best Performing Store : **{best_store.store_id}**

• Top Selling SKU : **{best_product.item_id}**

• Total Units Sold : **{total_sales:,}**

• Weekly Average Sales : **{avg_sales}**
""")