from pathlib import Path

import joblib
import pandas as pd
import streamlit as st
# ============================================================
# Project Paths
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"

OUTPUT_DIR = ROOT_DIR / "outputs"

MODEL_DIR = PROCESSED_DIR / "models"

# ============================================================
# Load Forecast Data
# ============================================================

@st.cache_data
def load_forecast():

    return pd.read_parquet(
        PROCESSED_DIR / "weekly_forecasts.parquet"
    )


# ============================================================
# Load Risk Results
# ============================================================

@st.cache_data
def load_risk():

    return pd.read_csv(
        OUTPUT_DIR / "risk_scoring_results.csv"
    )


# ============================================================
# Load Decision Summary
# ============================================================

@st.cache_data
def load_summary():

    return pd.read_csv(
        OUTPUT_DIR / "decision_summary.csv"
    )


# ============================================================
# Load Model
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(
        MODEL_DIR / "random_forest_forecaster.pkl"
    )