# 🔭 Project FORESIGHT
## AI-Powered Demand Forecasting & Inventory Intelligence Platform

<p align="center">
  <b>Turning historical retail data into demand forecasts, inventory risk insights, and actionable business decisions.</b>
</p>

<p align="center">
  <a href="https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Dashboard-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Live Dashboard">
  </a>
  <a href="https://github.com/PragzzX/Project_Foresight">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green?style=for-the-badge" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
</p>

---

## 📌 Overview

**Project FORESIGHT** is an end-to-end AI-powered demand forecasting and inventory intelligence platform designed to transform large-scale retail sales data into actionable business insights.

The platform combines:

- Historical sales analysis
- Data engineering
- Feature engineering
- Demand forecasting
- Machine learning
- Forecast evaluation
- Inventory risk scoring
- Product-level analysis
- Interactive dashboards
- Business intelligence

The main objective is to help retail planning teams answer three important questions:

> **What is likely to sell?**

> **How much inventory may be required?**

> **Where is the risk of stockout or overstock?**

FORESIGHT connects historical data with machine learning forecasts and inventory risk analytics to support smarter planning, replenishment, and inventory decisions.

---

# 🚀 Live Application

## 🌐 Live Streamlit Dashboard

### 👉 [Open Project FORESIGHT Dashboard](https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/)

The deployed dashboard provides interactive views for:

- 📊 Sales Analytics
- 🔮 Demand Forecasting
- 📦 Inventory Dashboard
- ⚠️ Risk Dashboard
- 🔎 Product Details
- 📋 Executive Summary

---

# 🎯 Project Objectives

The project was developed with the following objectives:

1. Analyze historical retail sales patterns.
2. Build a scalable data preparation pipeline.
3. Transform large-scale retail data into an analytical format.
4. Engineer temporal and demand-related features.
5. Establish a Seasonal Naive forecasting baseline.
6. Develop a machine learning demand forecasting model.
7. Evaluate forecasting performance using WAPE.
8. Convert forecasts into inventory risk indicators.
9. Identify potential stockout and overstock conditions.
10. Build an interactive business intelligence dashboard.
11. Present analytical results in a decision-oriented format.

---

# 🏗️ Solution Architecture

```text
                    ┌─────────────────────────┐
                    │       M5 Sales Data     │
                    │   Historical Retail Data│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Data Ingestion     │
                    │     & Transformation    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Feature Engineering  │
                    │                         │
                    │ • Calendar Features     │
                    │ • Price Dynamics        │
                    │ • Event Indicators      │
                    │ • Lag Features          │
                    │ • Rolling Statistics    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Demand Forecasting    │
                    │                         │
                    │ Seasonal Naive Baseline │
                    │          +              │
                    │ Random Forest Regressor │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Forecast Evaluation  │
                    │                         │
                    │          WAPE           │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Inventory Risk       │
                    │        Scoring          │
                    │                         │
                    │ • Stockout              │
                    │ • Overstock             │
                    │ • Healthy               │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Streamlit Dashboard   │
                    │                         │
                    │ • Sales Analytics       │
                    │ • Forecast Dashboard    │
                    │ • Inventory Dashboard   │
                    │ • Risk Dashboard        │
                    │ • Product Details       │
                    │ • Executive Summary     │
                    └─────────────────────────┘
````

---

# 📊 Dataset

The project uses the **M5 Forecasting dataset**, containing historical retail sales information across multiple stores and products.

## Dataset Characteristics

| Attribute         | Description                  |
| ----------------- | ---------------------------- |
| Dataset           | M5 Forecasting               |
| Stores            | 10                           |
| States            | California, Texas, Wisconsin |
| SKUs              | 30,490                       |
| Historical Period | 2011–2016                    |
| Primary Use       | Demand Forecasting           |
| Forecast Target   | Product Demand / Sales       |

The original wide-format sales data was transformed into a long-format analytical structure to make it suitable for large-scale feature engineering and machine learning.

---

# 🔄 Data Engineering Pipeline

The data preparation pipeline was designed to process the large-scale M5 dataset efficiently.

## Processing Workflow

```text
Raw M5 Dataset
      ↓
Data Cleaning
      ↓
Wide-to-Long Transformation
      ↓
Chunk-Based Processing
      ↓
Weekly Aggregation
      ↓
Feature Engineering
      ↓
Model-Ready Dataset
```

## Data Transformation

The wide-format sales data was transformed into a long-format structure containing approximately:

**58.3 million records**

The processing pipeline used chunk-based transformation to make large-scale processing more manageable.

After weekly aggregation, the analytical dataset contained approximately:

**10.15 million SKU-store observations**

---

# 🧠 Feature Engineering

Feature engineering was a major component of the forecasting pipeline.

The project created several groups of predictive features.

## 📅 Calendar Features

Calendar-based variables were created to capture temporal demand patterns.

Examples include:

* Week-related information
* Weekend indicators
* Seasonal signals
* Time-based patterns

## 💰 Price Features

Price-related variables were incorporated to capture the effect of pricing dynamics on demand.

## 🎉 Event Features

Event and calendar indicators were incorporated to capture demand changes associated with special events and periods.

## ⏮️ Lag Features

Historical demand values were used to capture temporal dependencies.

```text
lag_1
lag_2
lag_4
lag_8
```

These features provide the model with information about previous demand observations.

## 📈 Rolling Features

Rolling demand statistics were generated to capture recent demand trends.

Important features included:

```text
rolling_mean_4
lag_1
is_weekend
```

---

# 🤖 Machine Learning

## Baseline Model

A **Seasonal Naive** forecasting approach was established as the baseline model.

The baseline used the previous-period demand:

```text
Forecast = lag_1
```

The purpose of the baseline was to establish a simple reference point against which the machine learning model could be evaluated.

---

# 🌲 Random Forest Regressor

The primary machine learning model used in FORESIGHT was the:

## Random Forest Regressor

### Model Configuration

```text
Number of Estimators : 100
Maximum Depth        : 15
```

A chronological train-test split was used to reduce the risk of future information leaking into the training data.

### Train/Test Split

```text
Training Data : 80%
Testing Data  : 20%
```

Approximate dataset sizes:

```text
Training Rows : 8,122,536
Testing Rows  : 2,030,634
```

---

# 📏 Model Evaluation

The primary forecasting evaluation metric used was:

## WAPE — Weighted Absolute Percentage Error

WAPE was selected to evaluate forecast accuracy across the demand dataset.

## Model Results

| Model                   |   WAPE |
| ----------------------- | -----: |
| Seasonal Naive Baseline | 71.41% |
| Random Forest Regressor | 59.05% |

## Performance Improvement

The Random Forest model reduced WAPE from:

```text
71.41%
   ↓
59.05%
```

This represents an improvement of approximately:

**12.36 percentage points**

The result indicates that the engineered features and Random Forest model provided a stronger forecasting signal compared with the simple baseline.

---

# 🔍 Feature Importance

The Random Forest model identified the following features as important contributors to forecasting performance:

| Feature          | Importance |
| ---------------- | ---------: |
| `rolling_mean_4` |     70.51% |
| `lag_1`          |     13.45% |
| `is_weekend`     |      6.41% |
| `rolling_std_4`  |      3.11% |
| `lag_8`          |      1.67% |
| `lag_2`          |      1.50% |
| `sell_price`     |      1.26% |
| `lag_4`          |      1.25% |
| `has_event`      |      0.52% |
| `has_snap`       |      0.31% |

### Key Observation

The high contribution of `rolling_mean_4` indicates that recent demand trends were particularly useful for predicting future demand.

---

# 📦 Inventory Risk Scoring

Demand forecasting alone does not directly answer inventory planning questions.

FORESIGHT therefore converts forecast outputs into inventory risk signals.

The inventory risk pipeline estimates inventory requirements and classifies products into different risk categories.

## Inventory Estimation

```text
Estimated Inventory
        =
Actual Demand × 1.5
```

## Safety Stock

```text
Safety Stock
        =
Forecast × 0.30
```

## Inventory Gap

```text
Inventory Gap
        =
Estimated Inventory - Forecast
```

The resulting inventory conditions are classified into three categories.

---

## 🔴 Stockout Risk

Potential insufficient inventory relative to expected demand.

**Priority:** High

**Recommended Action:** Increase reorder quantity / reorder immediately.

---

## 🟠 Overstock Risk

Potential excess inventory relative to expected demand.

**Priority:** Medium

**Recommended Action:** Reduce purchasing / apply discount / launch promotion.

---

## 🟢 Healthy Inventory

Inventory conditions within the defined acceptable range.

**Priority:** Low

**Recommended Action:** Maintain current inventory.

---

# 📊 Inventory Risk Results

The risk scoring pipeline produced the following results on the test dataset:

| Risk Category | Priority | SKU-Week Count |
| ------------- | -------- | -------------: |
| 🟢 Healthy    | Low      |        583,764 |
| 🟠 Overstock  | Medium   |        593,552 |
| 🔴 Stockout   | High     |        853,318 |
| **Total**     | —        |  **2,030,634** |

---

# 💰 Business Impact

The inventory risk engine identified two major financial exposure areas.

### 🔴 Sales at Risk

**₹4,505,995**

Potential sales exposure associated with stockout-risk SKU-weeks.

### 🟠 Locked Working Capital

**₹9,475,885**

Estimated capital tied up in overstock-risk inventory.

### Combined Financial Exposure

**₹13,981,880**

These indicators allow decision-makers to prioritize inventory actions based on potential operational and financial impact.

---

# 📈 Interactive Dashboard

FORESIGHT includes an interactive **Streamlit dashboard** designed to present analytical outputs in a business-friendly format.

## Dashboard Modules

### 🏠 1. Home

Provides an overview of the FORESIGHT platform, project purpose, and key information.

### 📊 2. Sales Analytics

Provides historical sales analysis and trend exploration.

Users can explore sales patterns and understand demand behavior.

### 🔮 3. Forecast Dashboard

Displays demand forecasting outputs and model-related insights.

### 📦 4. Inventory Dashboard

Provides inventory planning information based on demand forecasts.

### ⚠️ 5. Risk Dashboard

Displays:

* Stockout risk
* Overstock risk
* Healthy inventory
* Risk distribution
* Financial exposure
* Business impact indicators

### 🔎 6. Product Details

Provides product-level analytical information for deeper investigation.

### 📋 7. Executive Summary

Provides a high-level business view of the project's key findings and performance.

---

# 🛠️ Technology Stack

## Programming

* Python 3.10+

## Data Engineering

* Pandas
* NumPy
* PyArrow
* Parquet

## Machine Learning

* Scikit-learn
* Random Forest Regressor
* Joblib

## Visualization

* Matplotlib
* Seaborn
* Plotly

## Dashboard

* Streamlit

## Business Intelligence

* Power BI

## Development Tools

* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

---

# 📁 Project Structure

```text
Project_Foresight/
│
├── dashboard/
│   ├── app.py
│   ├── Home.py
│   ├── utils.py
│   │
│   └── pages/
│       ├── Sales_Analytics.py
│       ├── Forecast.py
│       ├── Inventory_Dashboard.py
│       ├── Risk_Dashboard.py
│       ├── Product_Details.py
│       └── Executive_Summary.py
│
├── data/
│   ├── interim/
│   │
│   └── processed/
│       ├── weekly_forecasts.parquet
│       ├── sales_long.parquet
│       ├── risk_scoring.parquet
│       └── ...
│
├── notebooks/
│   ├── 01_Data_Engineering_Validation.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Demand_Forecasting_Model.ipynb
│   ├── 05_Risk_Scoring.ipynb
│   ├── 06_Planning_Dashboard.ipynb
│   ├── 07_Deployed_Scoring_Service.ipynb
│   └── 08_Executive_Readout.ipynb
│
├── outputs/
│   ├── decision_summary.csv
│   └── risk_scoring_results.csv
│
├── reports/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔬 End-to-End Workflow

```text
                  HISTORICAL DATA
                        │
                        ▼
               ┌─────────────────┐
               │ Data Engineering│
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Feature         │
               │ Engineering     │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Demand          │
               │ Forecasting     │
               │                 │
               │ Random Forest   │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Model Evaluation│
               │                 │
               │ WAPE            │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Inventory Risk  │
               │ Scoring         │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Business        │
               │ Dashboard       │
               └─────────────────┘
```

---

# 💡 Key Business Insights

FORESIGHT demonstrates how machine learning can be integrated into inventory planning rather than being treated as an isolated prediction task.

### Key Findings

* Recent historical demand is a strong forecasting signal.
* Rolling demand features contributed significantly to model performance.
* `rolling_mean_4` was the most important feature at **70.51%**.
* Random Forest improved forecasting performance compared with the Seasonal Naive baseline.
* The evaluated test set contained **853,318 stockout-risk SKU-weeks**.
* Overstock risk represented approximately **₹9.48M** in estimated locked working capital.
* Stockout risk represented approximately **₹4.51M** in estimated sales at risk.
* Combining demand forecasting with inventory rules provides more actionable insights than forecasting alone.

---

# 📌 Key Project Outcomes

## Data Engineering

```text
58M+ transformed records
10M+ weekly SKU-store observations
64 chunk-based processing pipeline
Parquet-based storage
```

## Demand Forecasting

```text
Baseline WAPE : 71.41%
ML WAPE       : 59.05%
Improvement   : 12.36 percentage points
```

## Inventory Intelligence

```text
Healthy   : 583,764
Overstock : 593,552
Stockout  : 853,318
```

## Financial Risk Indicators

```text
Locked Capital : ₹9,475,885
Sales at Risk  : ₹4,505,995
Total Exposure : ₹13,981,880
```

---

# 📚 Notebooks

The project development process is organized into notebooks covering the complete analytics workflow.

| Notebook                               | Purpose                         |
| -------------------------------------- | ------------------------------- |
| `01_Data_Engineering_Validation.ipynb` | Data preparation and validation |
| `02_Exploratory_Data_Analysis.ipynb`   | Exploratory analysis            |
| `03_Feature_Engineering.ipynb`         | Feature creation                |
| `04_Demand_Forecasting_Model.ipynb`    | Demand forecasting              |
| `05_Risk_Scoring.ipynb`                | Inventory risk analysis         |
| `06_Planning_Dashboard.ipynb`          | Dashboard development           |
| `07_Deployed_Scoring_Service.ipynb`    | Deployment and scoring workflow |
| `08_Executive_Readout.ipynb`           | Executive-level insights        |

---

# 📦 Outputs

The project produces analytical outputs including:

* Forecast datasets
* Risk scoring results
* Decision summaries
* Processed Parquet datasets
* Model artifacts
* Dashboard-ready datasets

Example outputs:

```text
outputs/
├── decision_summary.csv
└── risk_scoring_results.csv
```

---

# 🚀 Running the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/PragzzX/Project_Foresight.git
```

## 2. Navigate into the project

```bash
cd Project_Foresight
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will normally be available locally at:

```text
http://localhost:8501
```

---

# 🌐 Deployment

The dashboard is deployed using **Streamlit Community Cloud**.

### Live Application

👉 [Project FORESIGHT Live Dashboard](https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/)

The deployed application presents the forecasting and inventory analytics through an interactive web interface.

---

# 📊 Example Decision Flow

FORESIGHT converts raw historical information into business-oriented decisions:

```text
Historical Sales
       ↓
Demand Patterns
       ↓
Feature Engineering
       ↓
Machine Learning Forecast
       ↓
Expected Demand
       ↓
Inventory Comparison
       ↓
Risk Classification
       ↓
Business Action
```

### Example: Stockout

```text
High Expected Demand
        +
Low Estimated Inventory
        ↓
   STOCKOUT RISK
        ↓
Prioritize Replenishment
```

### Example: Overstock

```text
Low Expected Demand
        +
High Estimated Inventory
        ↓
   OVERSTOCK RISK
        ↓
Review Inventory / Reduce Excess
```

---

# 🧩 Engineering Highlights

The project demonstrates practical skills across the complete analytics lifecycle.

## Data Engineering

* Large-scale data transformation
* Wide-to-long conversion
* Chunk-based processing
* Weekly aggregation
* Parquet-based data storage

## Data Analytics

* Exploratory data analysis
* Time-based analysis
* Demand pattern identification
* Business KPI analysis

## Machine Learning

* Feature engineering
* Baseline modelling
* Random Forest regression
* Chronological train/test validation
* WAPE-based model evaluation
* Feature importance analysis

## Inventory Analytics

* Forecast-driven inventory estimation
* Safety stock calculations
* Inventory gap analysis
* Risk classification
* Financial impact estimation

## Data Visualization

* Interactive dashboards
* KPI cards
* Forecast visualizations
* Risk distribution charts
* Product-level analysis

## Deployment

* Streamlit application
* GitHub-based project management
* Cloud deployment
* Reproducible dependency management

---

# 🔮 Future Enhancements

The current system provides a strong foundation for demand and inventory intelligence.

Potential improvements include:

## Advanced Forecasting

* XGBoost
* LightGBM
* Gradient Boosting
* Advanced time-series models
* Ensemble forecasting

## Automated Machine Learning

* Hyperparameter optimization
* Automated model selection
* Cross-validation strategies
* Model comparison pipelines

## Real-Time Intelligence

* Real-time inventory feeds
* Live sales ingestion
* Automated forecast updates
* Near real-time risk monitoring

## Intelligent Alerts

* Automated stockout alerts
* Overstock alerts
* Demand anomaly detection
* High-impact product notifications

## Recommendation Engine

The system could be extended from risk detection to recommended actions:

```text
Stockout Risk
      ↓
Recommended Replenishment

Overstock Risk
      ↓
Inventory Reduction Recommendation

Demand Increase
      ↓
Increase Safety Stock
```

## Production MLOps

Future production enhancements could include:

* Automated model retraining
* Model monitoring
* Data drift detection
* Model performance tracking
* CI/CD pipelines
* Cloud-based data pipelines
* API-based forecasting services

---

# 🏁 Conclusion

**Project FORESIGHT demonstrates an end-to-end approach to retail demand forecasting and inventory intelligence.**

The project moves beyond simply predicting demand by connecting:

```text
DATA
  ↓
FEATURES
  ↓
FORECAST
  ↓
RISK
  ↓
BUSINESS DECISION
```

By combining large-scale data engineering, feature engineering, machine learning forecasting, inventory risk scoring, and interactive visualization, FORESIGHT provides a practical framework for converting historical retail data into forward-looking planning insights.

The Random Forest forecasting model achieved a WAPE of **59.05%**, improving upon the Seasonal Naive baseline of **71.41%**.

The inventory risk layer further translated forecasts into actionable categories:

* 🔴 Stockout
* 🟠 Overstock
* 🟢 Healthy Inventory

This makes FORESIGHT more than a forecasting model — it is an integrated **decision-support platform for retail demand and inventory planning**.

---

# 👩‍💻 Author

## L Pragna

**Data Analytics & Machine Learning Project**

Project FORESIGHT covers:

* Data Engineering
* Data Analytics
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning
* Demand Forecasting
* Inventory Risk Analytics
* Dashboard Development
* Business Intelligence
* Deployment

---

# 🔗 Project Links

### 📂 GitHub Repository

[Project FORESIGHT on GitHub](https://github.com/PragzzX/Project_Foresight)

### 🌐 Live Streamlit Dashboard

[Open Live Dashboard](https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/)

---

# ⭐ Project Status

| Component                 | Status      |
| ------------------------- | ----------- |
| Data Engineering          | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Feature Engineering       | ✅ Completed |
| Demand Forecasting        | ✅ Completed |
| Random Forest Model       | ✅ Completed |
| Model Evaluation          | ✅ Completed |
| Inventory Risk Scoring    | ✅ Completed |
| Dashboard                 | ✅ Completed |
| Streamlit Deployment      | 🟢 Live     |
| Executive Analysis        | ✅ Completed |

---

<p align="center">

### 🔭 Project FORESIGHT

<b>From Historical Data to Forward-Looking Decisions.</b>

<br><br>

Built with Python • Pandas • Scikit-learn • Plotly • Streamlit

</p>
```

