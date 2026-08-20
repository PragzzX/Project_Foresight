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
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

RISK_FILE = (
    ROOT_DIR
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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Main spacing ---------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }


    /* ---------- Hero ---------- */

    .hero {
        background: linear-gradient(
            135deg,
            #172554 0%,
            #2563eb 100%
        );

        padding: 30px 34px;
        border-radius: 18px;
        color: white;
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 34px;
        font-weight: 750;
        margin: 0 0 5px 0;
    }

    .hero-subtitle {
        font-size: 17px;
        font-weight: 500;
        margin-bottom: 8px;
        opacity: 0.95;
    }

    .hero-description {
        font-size: 14px;
        line-height: 1.55;
        max-width: 950px;
        opacity: 0.86;
    }


    /* ---------- Section titles ---------- */

    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #172554;
        margin: 22px 0 10px 0;
    }


    /* ---------- KPI cards ---------- */

    .kpi-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 17px 18px;
        min-height: 105px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .kpi-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 650;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .kpi-value {
        color: #172554;
        font-size: 28px;
        font-weight: 800;
        margin-top: 7px;
    }


    /* ---------- Insight card ---------- */

    .insight-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 22px;
        min-height: 320px;
    }

    .insight-title {
        color: #172554;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .insight-text {
        color: #475569;
        font-size: 14px;
        line-height: 1.65;
    }


    /* ---------- Action cards ---------- */

    .action-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px;
        min-height: 145px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .action-title {
        color: #334155;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .action-number {
        color: #172554;
        font-size: 27px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .action-description {
        color: #64748b;
        font-size: 12px;
        line-height: 1.45;
    }


    /* ---------- Health score ---------- */

    .score-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 22px;
        text-align: center;
    }

    .score-value {
        font-size: 40px;
        font-weight: 800;
        color: #2563eb;
    }

    .score-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 600;
    }


    /* ---------- Methodology ---------- */

    .method-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px 20px;
        color: #475569;
        font-size: 13px;
        line-height: 1.6;
    }

    .method-step {
        margin-bottom: 7px;
    }

    .method-step strong {
        color: #172554;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title">
            📈 Project FORESIGHT
        </div>

        <div class="hero-subtitle">
            AI-Powered Retail Demand & Inventory Intelligence
        </div>

        <div class="hero-description">
            A decision-intelligence platform combining historical
            sales, machine-learning demand forecasts and inventory
            risk scoring to support smarter retail planning,
            replenishment and inventory decisions.
        </div>

    </div>
    """
)


# ============================================================
# DATA VALIDATION
# ============================================================

if risk_df is None:

    st.error("❌ Risk scoring data could not be loaded.")

    st.write("Expected file:")

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
    "inventory_risk",
]:
    if column in risk_df.columns:
        risk_column = column
        break


# ============================================================
# RISK METRICS
# ============================================================

total_products = len(risk_df)

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
# PERCENTAGES
# ============================================================

if total_products > 0:

    healthy_pct = (
        healthy / total_products
    ) * 100

    at_risk_pct = (
        at_risk / total_products
    ) * 100

else:

    healthy_pct = 0
    at_risk_pct = 0


# ============================================================
# INVENTORY HEALTH SCORE
# ============================================================

health_score = round(healthy_pct)


# ============================================================
# 1. KPI ROW
# ============================================================

st.markdown(
    '<div class="section-title">📊 Intelligence Snapshot</div>',
    unsafe_allow_html=True,
)

k1, k2, k3, k4 = st.columns(4)


with k1:
    st.html(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Products Analysed</div>
            <div class="kpi-value">{total_products:,}</div>
        </div>
        """
    )


with k2:
    st.html(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Healthy Inventory</div>
            <div class="kpi-value">{healthy_pct:.1f}%</div>
        </div>
        """
    )


with k3:
    st.html(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">At-Risk Products</div>
            <div class="kpi-value">{at_risk:,}</div>
        </div>
        """
    )


with k4:
    st.html(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Stockout Risk</div>
            <div class="kpi-value">{stockout:,}</div>
        </div>
        """
    )


# ============================================================
# 2. RISK OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">🎯 Inventory Risk Overview</div>',
    unsafe_allow_html=True,
)

chart_col, insight_col = st.columns([1.05, 1])


# ============================================================
# DONUT CHART
# ============================================================

with chart_col:

    if risk_column:

        chart_data = pd.DataFrame(
            {
                "Risk": [
                    "Healthy",
                    "Overstock",
                    "Stockout",
                ],
                "Products": [
                    healthy,
                    overstock,
                    stockout,
                ],
            }
        )

        chart_data = chart_data[
            chart_data["Products"] > 0
        ]

        fig = px.pie(
            chart_data,
            names="Risk",
            values="Products",
            hole=0.64,
        )

        fig.update_traces(
            textinfo="percent+label",
            hovertemplate=(
                "<b>%{label}</b>"
                "<br>Products: %{value:,}"
                "<br>Share: %{percent}"
                "<extra></extra>"
            ),
        )

        fig.update_layout(
            height=330,
            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10,
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.08,
                xanchor="center",
                x=0.5,
            ),
        )

        st.plotly_chart(
            fig,
            width="stretch",
        )

    else:

        st.warning(
            "No risk classification column was found."
        )


# ============================================================
# BUSINESS INSIGHT
# ============================================================

with insight_col:

    if overstock > stockout:

        insight_title = "🟠 Overstock is the dominant risk"

        insight_text = (
            f"{overstock:,} products are classified as "
            f"overstock, compared with {stockout:,} "
            f"stockout-risk products."
        )

        recommendation = (
            "Review slow-moving inventory, purchasing levels "
            "and promotional opportunities to reduce excess stock."
        )

    elif stockout > overstock:

        insight_title = "🔴 Stockout is the dominant risk"

        insight_text = (
            f"{stockout:,} products are classified as "
            f"stockout risk, compared with {overstock:,} "
            f"overstock-risk products."
        )

        recommendation = (
            "Prioritize replenishment and review safety-stock "
            "levels for products exposed to stockout risk."
        )

    else:

        insight_title = "⚖️ Inventory risks are balanced"

        insight_text = (
            f"Stockout and overstock risks are relatively "
            f"balanced at {stockout:,} and {overstock:,} products."
        )

        recommendation = (
            "Continue monitoring demand and inventory signals "
            "to prevent either risk category from increasing."
        )

    st.html(
        f"""
        <div class="insight-card">

            <div class="insight-title">
                {insight_title}
            </div>

            <div class="insight-text">

                <p>
                    {insight_text}
                </p>

                <p>
                    <strong>Healthy inventory:</strong>
                    {healthy:,} products ({healthy_pct:.1f}%)
                </p>

                <p>
                    <strong>At-risk inventory:</strong>
                    {at_risk:,} products ({at_risk_pct:.1f}%)
                </p>

                <p>
                    <strong>Recommended focus:</strong><br>
                    {recommendation}
                </p>

            </div>

        </div>
        """
    )


# ============================================================
# 3. INVENTORY HEALTH
# ============================================================

st.markdown(
    '<div class="section-title">💚 Inventory Health</div>',
    unsafe_allow_html=True,
)

score_col, explanation_col = st.columns([0.7, 1.3])


with score_col:

    st.html(
        f"""
        <div class="score-card">

            <div class="score-value">
                {health_score}/100
            </div>

            <div class="score-label">
                INVENTORY HEALTH SCORE
            </div>

        </div>
        """
    )


with explanation_col:

    st.info(
        f"""
        **Current health: {healthy_pct:.1f}%**

        {healthy:,} of {total_products:,} analysed records are
        classified as healthy inventory.

        **At risk:** {at_risk:,} records
        ({at_risk_pct:.1f}%)
        """
    )


# ============================================================
# 4. PRIORITY ACTIONS
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Priority Actions</div>',
    unsafe_allow_html=True,
)

a1, a2, a3 = st.columns(3)


with a1:

    st.html(
        f"""
        <div class="action-card">

            <div class="action-title">
                🔴 Stockout Risk
            </div>

            <div class="action-number">
                {stockout:,}
            </div>

            <div class="action-description">
                Prioritize replenishment and review
                safety-stock levels.
            </div>

        </div>
        """
    )


with a2:

    st.html(
        f"""
        <div class="action-card">

            <div class="action-title">
                🟠 Overstock Risk
            </div>

            <div class="action-number">
                {overstock:,}
            </div>

            <div class="action-description">
                Review purchasing, slow-moving stock
                and promotional opportunities.
            </div>

        </div>
        """
    )


with a3:

    st.html(
        f"""
        <div class="action-card">

            <div class="action-title">
                🟢 Healthy Inventory
            </div>

            <div class="action-number">
                {healthy:,}
            </div>

            <div class="action-description">
                Continue monitoring demand and
                inventory signals.
            </div>

        </div>
        """
    )


# ============================================================
# 5. WHAT FORESIGHT ANSWERS
# ============================================================

st.markdown(
    '<div class="section-title">🧠 What FORESIGHT Answers</div>',
    unsafe_allow_html=True,
)

q1, q2, q3 = st.columns(3)


with q1:

    st.html(
        """
        <div class="action-card">

            <div class="action-title">
                📈 What will demand look like?
            </div>

            <div class="action-description">
                Machine-learning forecasting identifies
                expected future demand patterns from
                historical sales and engineered signals.
            </div>

        </div>
        """
    )


with q2:

    st.html(
        """
        <div class="action-card">

            <div class="action-title">
                ⚠️ Where is inventory at risk?
            </div>

            <div class="action-description">
                Risk scoring highlights products exposed
                to potential stockout and overstock conditions.
            </div>

        </div>
        """
    )


with q3:

    st.html(
        """
        <div class="action-card">

            <div class="action-title">
                📦 What should we do?
            </div>

            <div class="action-description">
                The resulting intelligence supports
                replenishment, purchasing and inventory
                management decisions.
            </div>

        </div>
        """
    )


# ============================================================
# 6. HOW FORESIGHT WORKS
# ============================================================

st.markdown(
    '<div class="section-title">🔍 How FORESIGHT Works</div>',
    unsafe_allow_html=True,
)

st.html(
    """
    <div class="method-card">

        <div class="method-step">
            <strong>01 · Data Preparation</strong>
            —
            Historical sales and inventory data are
            cleaned and validated.
        </div>

        <div class="method-step">
            <strong>02 · Feature Engineering</strong>
            —
            Demand signals, lag features, rolling statistics
            and calendar features are generated.
        </div>

        <div class="method-step">
            <strong>03 · Demand Forecasting</strong>
            —
            Machine-learning models estimate future demand.
        </div>

        <div class="method-step">
            <strong>04 · Risk Scoring</strong>
            —
            Inventory signals are evaluated to identify
            stockout and overstock conditions.
        </div>

        <div class="method-step">
            <strong>05 · Decision Support</strong>
            —
            Forecast and risk intelligence is presented
            for smarter replenishment and inventory planning.
        </div>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    f"Project FORESIGHT  •  "
    f"{total_products:,} records analysed  •  "
    f"Source: risk_scoring.parquet"
)