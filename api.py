from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

import joblib
import pandas as pd
from huggingface_hub import hf_hub_download


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent

MODEL_REPO = "pragnal7512/foresight-random-forest"
MODEL_FILE = "random_forest_forecaster.pkl"


# ============================================================
# LOAD MODEL FROM HUGGING FACE
# ============================================================

print("Loading Random Forest model from Hugging Face...")

try:
    MODEL_PATH = hf_hub_download(
        repo_id=MODEL_REPO,
        filename=MODEL_FILE
    )

    model = joblib.load(MODEL_PATH)

    print("Model loaded successfully.")
    print(f"Model path: {MODEL_PATH}")

except Exception as e:
    print(f"Failed to load model: {e}")
    raise RuntimeError(
        f"Unable to load Random Forest model: {e}"
    )


# ============================================================
# MODEL FEATURES
# ============================================================

FEATURES = [
    "sell_price",
    "has_event",
    "has_snap",
    "is_weekend",
    "lag_1",
    "lag_2",
    "lag_4",
    "lag_8",
    "rolling_mean_4",
    "rolling_std_4"
]


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Project FORESIGHT Scoring Service",
    description="Forecast and inventory risk prediction API",
    version="1.0.0"
)


# ============================================================
# REQUEST SCHEMAS
# ============================================================

class ForecastRequest(BaseModel):

    sell_price: float
    has_event: int
    has_snap: int
    is_weekend: int
    lag_1: float
    lag_2: float
    lag_4: float
    lag_8: float
    rolling_mean_4: float
    rolling_std_4: float


class RiskRequest(BaseModel):

    estimated_inventory: float
    safety_stock: float
    forecast: float


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():

    return {
        "service": "Project FORESIGHT Scoring Service",
        "status": "online",
        "docs": "/docs",
        "health": "/health"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Project FORESIGHT Scoring Service",
        "model_loaded": model is not None
    }


# ============================================================
# FORECAST API
# ============================================================

@app.post("/predict/forecast")
def predict_forecast(request: ForecastRequest):

    try:

        input_data = pd.DataFrame([{

            "sell_price": request.sell_price,
            "has_event": request.has_event,
            "has_snap": request.has_snap,
            "is_weekend": request.is_weekend,
            "lag_1": request.lag_1,
            "lag_2": request.lag_2,
            "lag_4": request.lag_4,
            "lag_8": request.lag_8,
            "rolling_mean_4": request.rolling_mean_4,
            "rolling_std_4": request.rolling_std_4

        }])

        # Ensure exact feature order
        input_data = input_data[FEATURES]

        prediction = model.predict(input_data)

        return {
            "forecast": float(prediction[0])
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# RISK API
# ============================================================

@app.post("/predict/risk")
def predict_risk(request: RiskRequest):

    inventory_gap = (
        request.estimated_inventory
        - request.safety_stock
    )

    # --------------------------------------------------------
    # STOCKOUT RISK
    # --------------------------------------------------------

    if inventory_gap < 0:

        risk = "Stockout Risk"
        priority = "High"
        decision = "Reorder Immediately"
        recommended_action = "Increase replenishment"

    # --------------------------------------------------------
    # OVERSTOCK RISK
    # --------------------------------------------------------

    elif request.estimated_inventory > (
        request.forecast * 1.5
    ):

        risk = "Overstock Risk"
        priority = "Medium"
        decision = "Reduce Purchasing / Launch Promotion"
        recommended_action = (
            "Reduce purchasing or promote stock"
        )

    # --------------------------------------------------------
    # HEALTHY
    # --------------------------------------------------------

    else:

        risk = "Healthy"
        priority = "Low"
        decision = "Maintain Current Inventory"
        recommended_action = (
            "Maintain current inventory"
        )

    return {

        "risk": risk,
        "priority": priority,
        "decision": decision,
        "recommended_action": recommended_action,
        "inventory_gap": inventory_gap

    }