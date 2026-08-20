import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Project FORESIGHT",
    page_icon="📈",
    layout="wide"
)


# ============================================================
# DATA PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RISK_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "risk_scoring.parquet"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_risk_data():

    if not RISK_FILE.exists():
        return None

    return pd.read_parquet(RISK_FILE)


risk_df = load_risk_data()


# ============================================================
# HEADER
# ============================================================

st.title("📈 Project FORESIGHT")

st.subheader(
    "AI-Powered Retail Demand & Inventory Intelligence"
)

st.write(
    """
    FORESIGHT combines demand forecasting and inventory risk
    analysis to help identify what is likely to happen next
    and where inventory decisions require attention.
    """
)

st.divider()


# ============================================================
# DATA CHECK
# ============================================================

if risk_df is None:

    st.error("❌ Risk scoring data could not be loaded.")

    st.code(str(RISK_FILE))

    st.stop()


# ============================================================
# NORMALIZE COLUMNS
# ============================================================

risk_df.columns = [
    str(column).strip().lower()
    for column in risk_df.columns
]


# ============================================================
# FIND RISK COLUMN
# ============================================================

risk_column = None

for column in [
    "risk",
    "risk_category",
    "risk_level",
    "inventory_risk"
]:

    if column in risk_df.columns:
        risk_column = column
        break


# ============================================================
# RISK METRICS
# ============================================================

total_records = len(risk_df)

healthy = 0
overstock = 0
stockout = 0

if risk_column:

    risk_values = (
        risk_df[risk_column]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    healthy = int(
        risk_values.str.contains(
            "healthy",
            na=False
        ).sum()
    )

    overstock = int(
        risk_values.str.contains(
            "overstock",
            na=False
        ).sum()
    )

    stockout = int(
        risk_values.str.contains(
            "stockout",
            na=False
        ).sum()
    )


at_risk = overstock + stockout


# ============================================================
# KPI CARDS
# ============================================================

st.markdown("### 📊 Intelligence Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Records Analysed",
        f"{total_records:,}"
    )

with col2:

    st.metric(
        "Healthy",
        f"{healthy:,}"
    )

with col3:

    st.metric(
        "At Risk",
        f"{at_risk:,}"
    )

with col4:

    st.metric(
        "Stockout Risk",
        f"{stockout:,}"
    )


st.divider()


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.markdown("### 🎯 Inventory Risk Distribution")

if risk_column:

    chart_data = pd.DataFrame({
        "Risk": [
            "Healthy",
            "Overstock",
            "Stockout"
        ],
        "Products": [
            healthy,
            overstock,
            stockout
        ]
    })

    chart_data = chart_data[
        chart_data["Products"] > 0
    ]

    fig = px.pie(
        chart_data,
        names="Risk",
        values="Products",
        hole=0.60
    )

    fig.update_layout(
        height=420,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.warning(
        "No risk classification column was found."
    )


# ============================================================
# WHAT FORESIGHT DOES
# ============================================================

st.divider()

st.markdown("### 🧠 What FORESIGHT Helps Answer")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        **📈 What will demand look like?**

        Machine-learning forecasting helps estimate
        future demand using historical sales patterns
        and engineered demand features.
        """
    )


with col2:

    st.markdown(
        """
        **⚠️ Where is inventory at risk?**

        Risk scoring identifies potential stockout
        and overstock situations that may require
        intervention.
        """
    )


with col3:

    st.markdown(
        """
        **📦 What should we do?**

        The resulting intelligence supports better
        replenishment, purchasing and inventory
        management decisions.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    f"Project FORESIGHT • "
    f"{total_records:,} records analysed"
)