import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Project FORESIGHT")

st.markdown("---")

st.header("Retail Demand Forecasting & Inventory Intelligence")

st.write(
"""
Project FORESIGHT helps retail teams:

- Forecast weekly demand
- Detect stockout risk
- Detect overstock risk
- Estimate business impact
- Recommend inventory actions
"""
)

col1, col2, col3 = st.columns(3)

col1.metric("Notebook Pipeline", "5 Completed")

col2.metric("Forecast Model", "Random Forest")

col3.metric("Forecast Accuracy", "WAPE 0.5905")

st.success("Navigate using the sidebar to explore analytics.")