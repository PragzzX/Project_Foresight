import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Product Details",
    page_icon="📦",
    layout="wide"
)

# ============================================================
# PATHS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = ROOT_DIR / "data" / "processed"

# ============================================================
# LOAD DATA
# ============================================================

# Product Details only uses risk_scoring.parquet.
# weekly_forecasts.parquet is not needed on this page.
@st.cache_data(show_spinner=False)
def load_data():

    risk = pd.read_parquet(
        PROCESSED_DIR / "risk_scoring.parquet"
    )

    return risk


risk_df = load_data()

# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.metric-card{
    background:#ffffff;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
    border-left:6px solid #2563eb;
}

.big-font{
    font-size:30px;
    font-weight:700;
}

.small-font{
    color:gray;
    font-size:14px;
}

.risk-high{
    background:#ffebee;
    color:#c62828;
    padding:12px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
}

.risk-medium{
    background:#fff8e1;
    color:#ef6c00;
    padding:12px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
}

.risk-low{
    background:#e8f5e9;
    color:#2e7d32;
    padding:12px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# TITLE
# ============================================================

st.title("📦 Product Details")

st.caption(
    "SKU-level forecasting, inventory planning and risk assessment."
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Filters")

store = st.sidebar.selectbox(
    "Store",
    sorted(risk_df.store_id.unique())
)

product_list = sorted(
    risk_df.loc[
        risk_df.store_id == store,
        "item_id"
    ].unique()
)

sku = st.sidebar.selectbox(
    "Product",
    product_list
)

product_df = risk_df[
    (risk_df.store_id == store) &
    (risk_df.item_id == sku)
].copy()

week = st.sidebar.selectbox(
    "Week",
    sorted(
        product_df.week_of_year.unique()
    )
)

selected = product_df[
    product_df.week_of_year == week
].iloc[0]

# ============================================================
# KPI SECTION
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Forecast",
    f"{selected.rf_forecast:,.0f}"
)

c2.metric(
    "Inventory",
    f"{selected.estimated_inventory:,.0f}"
)

c3.metric(
    "Safety Stock",
    f"{selected.safety_stock:,.0f}"
)

c4.metric(
    "Inventory Gap",
    f"{selected.inventory_gap:,.0f}"
)

c5.metric(
    "Sell Price",
    f"₹ {selected.sell_price:,.2f}"
)

st.divider()

# ============================================================
# RISK STATUS
# ============================================================

if selected.risk == "Stockout Risk":

    st.markdown(
        f"""
<div class="risk-high">

🚨 HIGH RISK

<br><br>

{selected.decision}

</div>
""",
        unsafe_allow_html=True
    )

elif selected.risk == "Overstock Risk":

    st.markdown(
        f"""
<div class="risk-medium">

⚠️ OVERSTOCK RISK

<br><br>

{selected.decision}

</div>
""",
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
<div class="risk-low">

✅ HEALTHY INVENTORY

<br><br>

Maintain Current Inventory

</div>
""",
        unsafe_allow_html=True
    )

st.divider()

# ============================================================
# FORECAST HISTORY
# ============================================================

history = product_df.sort_values(
    "week_of_year"
)

fig = px.line(
    history,
    x="week_of_year",
    y=[
        "units_sold",
        "rf_forecast"
    ],
    markers=True,
    title="Weekly Actual Sales vs Forecast"
)

fig.update_layout(
    height=450,
    legend_title=""
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ============================================================
# INVENTORY CHART
# ============================================================

inventory = go.Figure()

inventory.add_trace(
    go.Bar(
        x=history.week_of_year,
        y=history.estimated_inventory,
        name="Inventory"
    )
)

inventory.add_trace(
    go.Scatter(
        x=history.week_of_year,
        y=history.safety_stock,
        mode="lines+markers",
        name="Safety Stock"
    )
)

inventory.update_layout(
    title="Inventory vs Safety Stock",
    height=450
)

st.plotly_chart(
    inventory,
    width="stretch"
)

st.divider()

# ============================================================
# INVENTORY GAP ANALYSIS
# ============================================================

st.subheader("📊 Inventory Gap Analysis")

gap_col1, gap_col2 = st.columns([2, 1])

with gap_col1:

    gap_fig = go.Figure()

    gap_fig.add_trace(
        go.Bar(
            x=history["week_of_year"],
            y=history["inventory_gap"],
            marker_color=[
                "#EF4444" if x < 0 else "#10B981"
                for x in history["inventory_gap"]
            ],
            text=history["inventory_gap"].round(0),
            textposition="outside"
        )
    )

    gap_fig.update_layout(
        title="Inventory Gap by Week",
        xaxis_title="Week",
        yaxis_title="Inventory Gap",
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        gap_fig,
        width="stretch"
    )

with gap_col2:

    st.metric(
        "Current Gap",
        f"{selected.inventory_gap:,.0f}"
    )

    if selected.inventory_gap < 0:

        st.error(
            "Inventory below safety stock.\n\n"
            "Immediate replenishment recommended."
        )

    elif selected.inventory_gap > 0:

        st.success(
            "Inventory above safety stock."
        )

    else:

        st.info(
            "Inventory exactly matches safety stock."
        )

# ============================================================
# BUSINESS IMPACT
# ============================================================

st.divider()

st.subheader("💰 Financial Impact")

m1, m2, m3 = st.columns(3)

m1.metric(
    "Sales At Risk",
    f"₹ {selected.sales_at_risk_rs:,.0f}"
)

m2.metric(
    "Locked Capital",
    f"₹ {selected.locked_capital_rs:,.0f}"
)

m3.metric(
    "Priority",
    selected.priority
)

# ============================================================
# RECOMMENDATION PANEL
# ============================================================

st.divider()

st.subheader("🎯 Recommended Business Action")

recommendation_color = {
    "High": "#FEE2E2",
    "Medium": "#FEF3C7",
    "Low": "#DCFCE7"
}

border_color = {
    "High": "#DC2626",
    "Medium": "#F59E0B",
    "Low": "#16A34A"
}

st.markdown(
    f"""
<div style="
background:{recommendation_color[selected.priority]};
padding:25px;
border-left:8px solid {border_color[selected.priority]};
border-radius:12px;
">

<h3>{selected.decision}</h3>

<b>Risk Level:</b> {selected.risk}<br>

<b>Recommended Action:</b> {selected.recommended_action}

</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# PRODUCT SUMMARY
# ============================================================

st.divider()

st.subheader("📦 Product Summary")

summary = pd.DataFrame({

    "Metric": [
        "Store",
        "Product",
        "Week",
        "Forecast",
        "Actual Sales",
        "Estimated Inventory",
        "Safety Stock",
        "Inventory Gap",
        "Risk",
        "Priority",
        "Decision"
    ],

    "Value": [
        selected.store_id,
        selected.item_id,
        selected.week_of_year,
        round(selected.rf_forecast, 2),
        round(selected.units_sold, 2),
        round(selected.estimated_inventory, 2),
        round(selected.safety_stock, 2),
        round(selected.inventory_gap, 2),
        selected.risk,
        selected.priority,
        selected.decision
    ]

})

st.dataframe(
    summary,
    width="stretch",
    hide_index=True
)

# ============================================================
# DOWNLOAD DATA
# ============================================================

st.divider()

csv = product_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Product Report",
    csv,
    file_name=f"{sku}_report.csv",
    mime="text/csv"
)

# ============================================================
# PRODUCT HISTORY
# ============================================================

st.divider()

st.subheader("📋 Complete Weekly History")

display_cols = [
    "week_of_year",
    "units_sold",
    "rf_forecast",
    "estimated_inventory",
    "safety_stock",
    "inventory_gap",
    "risk",
    "priority"
]

st.dataframe(
    product_df[display_cols]
    .sort_values("week_of_year"),
    width="stretch",
    hide_index=True
)

# ============================================================
# PAGE FOOTER
# ============================================================

st.divider()

st.caption(
"""
Project FORESIGHT • Product Details Dashboard

This page provides SKU-level forecast performance,
inventory planning metrics,
financial impact,
risk classification,
and business recommendations
to support inventory decision-making.
"""
)