<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Project Foresight</title>

    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.7;
            color: #24292f;
            max-width: 1100px;
            margin: auto;
            padding: 40px;
            background: #ffffff;
        }

        h1 {
            color: #174a7e;
            font-size: 42px;
            margin-bottom: 5px;
        }

        h2 {
            color: #174a7e;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 8px;
            margin-top: 45px;
        }

        h3 {
            color: #2563eb;
            margin-top: 30px;
        }

        .subtitle {
            font-size: 20px;
            color: #666;
            margin-bottom: 25px;
        }

        .badge {
            display: inline-block;
            padding: 5px 12px;
            margin: 4px;
            border-radius: 15px;
            background: #eef4fb;
            color: #174a7e;
            font-size: 13px;
        }

        .hero {
            background: linear-gradient(135deg, #174a7e, #2563eb);
            color: white;
            padding: 35px;
            border-radius: 14px;
            margin-bottom: 35px;
        }

        .hero h1 {
            color: white;
        }

        .hero p {
            font-size: 18px;
        }

        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 25px 0;
        }

        .card {
            flex: 1;
            min-width: 210px;
            padding: 20px;
            border: 1px solid #e1e4e8;
            border-radius: 10px;
            background: #f8fafc;
        }

        .card h3 {
            margin-top: 0;
        }

        .metric {
            font-size: 27px;
            font-weight: bold;
            color: #174a7e;
        }

        .success {
            border-left: 5px solid #16a34a;
            padding: 15px 20px;
            background: #f0fdf4;
        }

        .warning {
            border-left: 5px solid #f59e0b;
            padding: 15px 20px;
            background: #fffbeb;
        }

        .danger {
            border-left: 5px solid #dc2626;
            padding: 15px 20px;
            background: #fef2f2;
        }

        pre {
            background: #0f172a;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
        }

        code {
            font-family: Consolas, Monaco, monospace;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        th {
            background: #174a7e;
            color: white;
            text-align: left;
            padding: 12px;
        }

        td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }

        tr:nth-child(even) {
            background: #f8fafc;
        }

        a {
            color: #2563eb;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .footer {
            margin-top: 60px;
            padding-top: 25px;
            border-top: 2px solid #e5e7eb;
            color: #666;
        }
    </style>
</head>

<body>

<!-- ================= HERO ================= -->

<div class="hero">

    <h1>🔮 Project Foresight</h1>

    <p>
        <strong>
            AI-Powered Retail Demand Forecasting & Inventory Risk
            Intelligence Platform
        </strong>
    </p>

    <p>
        An end-to-end data analytics and machine learning platform
        designed to transform historical retail sales data into
        demand forecasts, inventory risk insights and
        decision-support intelligence.
    </p>

</div>


<!-- ================= PROJECT OVERVIEW ================= -->

<h2>📌 Project Overview</h2>

<p>
    <strong>Project Foresight</strong> is an end-to-end retail analytics
    and machine learning project focused on two major business problems:
</p>

<div class="card-container">

    <div class="card">
        <h3>📈 Demand Forecasting</h3>

        <p>
            Predicting future product demand using historical
            sales patterns and engineered predictive features.
        </p>
    </div>

    <div class="card">
        <h3>⚠️ Inventory Risk Intelligence</h3>

        <p>
            Identifying products exposed to stockout and
            overstock risks and estimating their business impact.
        </p>
    </div>

</div>

<p>
    The project combines data engineering, exploratory data analysis,
    feature engineering, machine learning, forecasting, risk scoring
    and interactive visualization into a unified decision-support
    platform.
</p>


<!-- ================= BUSINESS PROBLEM ================= -->

<h2>🎯 Business Problem</h2>

<p>
    Retail organizations need to maintain sufficient inventory to
    satisfy customer demand while avoiding unnecessary excess stock.
</p>

<div class="danger">

    <h3>🔴 Stockout Risk</h3>

    <ul>
        <li>Lost sales</li>
        <li>Unmet customer demand</li>
        <li>Reduced customer satisfaction</li>
        <li>Potential revenue loss</li>
    </ul>

</div>

<div class="warning">

    <h3>🟠 Overstock Risk</h3>

    <ul>
        <li>Capital locked in inventory</li>
        <li>Higher storage costs</li>
        <li>Lower inventory turnover</li>
        <li>Operational inefficiency</li>
    </ul>

</div>

<p>
    Project Foresight addresses these challenges by connecting
    demand forecasting with inventory risk analysis.
</p>


<!-- ================= OBJECTIVES ================= -->

<h2>🚀 Project Objectives</h2>

<ul>
    <li>Analyze historical retail sales data.</li>
    <li>Identify sales and demand patterns.</li>
    <li>Perform data validation and transformation.</li>
    <li>Engineer predictive features.</li>
    <li>Develop machine-learning-based demand forecasting.</li>
    <li>Evaluate forecasting performance using WAPE.</li>
    <li>Generate demand forecasts.</li>
    <li>Classify inventory into risk categories.</li>
    <li>Identify stockout and overstock-prone products.</li>
    <li>Estimate financial exposure.</li>
    <li>Develop interactive business dashboards.</li>
    <li>Provide decision-support insights.</li>
</ul>


<!-- ================= ARCHITECTURE ================= -->

<h2>🏗️ Solution Architecture</h2>

<pre><code>
                    ┌──────────────────────┐
                    │   Historical Sales   │
                    │        Data          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Validation &    │
                    │ Data Preparation     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Exploratory Data     │
                    │ Analysis             │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Engineering  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
      ┌───────────────────┐        ┌────────────────────┐
      │ Demand Forecasting│        │ Inventory Risk     │
      │ Models            │        │ Scoring             │
      └─────────┬─────────┘        └──────────┬─────────┘
                │                             │
                ▼                             ▼
      ┌───────────────────┐        ┌────────────────────┐
      │ Forecast Results  │        │ Risk Classification│
      └─────────┬─────────┘        └──────────┬─────────┘
                │                             │
                └──────────────┬──────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Business KPIs &      │
                    │ Decision Intelligence│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────────────────┘
</code></pre>


<!-- ================= WORKFLOW ================= -->

<h2>📊 Analytical Workflow</h2>

<h3>1. Data Engineering & Validation</h3>

<p>
    The first stage prepares the source data for analytics and
    machine learning.
</p>

<ul>
    <li>Data loading</li>
    <li>Data validation</li>
    <li>Data cleaning</li>
    <li>Data transformation</li>
    <li>Data merging</li>
    <li>Preparation of processed datasets</li>
</ul>

<pre><code>
src/
└── data/
    ├── load_data.py
    ├── validate_data.py
    ├── transform_data.py
    └── merge_data.py
</code></pre>


<h3>2. Exploratory Data Analysis</h3>

<p>
    Exploratory analysis was performed to understand historical
    sales and demand behaviour.
</p>

<ul>
    <li>Sales trends</li>
    <li>Demand patterns</li>
    <li>Store-level behaviour</li>
    <li>Product-level behaviour</li>
    <li>Temporal patterns</li>
    <li>Sales distributions</li>
</ul>


<h3>3. Feature Engineering</h3>

<p>
    Historical sales information was transformed into predictive
    features suitable for forecasting.
</p>

<pre><code>
03_Feature_Engineering.ipynb
</code></pre>


<h3>4. Demand Forecasting</h3>

<p>
    The forecasting component estimates expected future demand
    from historical sales and engineered features.
</p>

<pre><code>
Historical Sales
       ↓
Feature Engineering
       ↓
Training Dataset
       ↓
Forecasting Model
       ↓
Model Evaluation
       ↓
Demand Forecast
</code></pre>


<!-- ================= MODEL ================= -->

<h2>🤖 Machine Learning</h2>

<h3>Random Forest Forecasting</h3>

<p>
    A Random Forest-based approach is used within the forecasting
    pipeline to model relationships between engineered variables
    and demand.
</p>

<p>
    The model is evaluated using <strong>WAPE
    (Weighted Absolute Percentage Error)</strong>.
</p>

<div class="card-container">

    <div class="card">
        <h3>Forecast Units</h3>
        <div class="metric">5,667,654</div>
    </div>

    <div class="card">
        <h3>Actual Units</h3>
        <div class="metric">5,223,487</div>
    </div>

    <div class="card">
        <h3>Random Forest WAPE</h3>
        <div class="metric">0.5905</div>
    </div>

    <div class="card">
        <h3>Improvement</h3>
        <div class="metric">17.3%</div>
    </div>

</div>


<!-- ================= RISK SCORING ================= -->

<h2>⚠️ Inventory Risk Scoring</h2>

<p>
    The inventory risk engine classifies products according to
    their inventory condition and potential operational risk.
</p>

<div class="card-container">

    <div class="card">
        <h3>🟢 Healthy</h3>
        <p>Inventory considered to be within a healthy range.</p>
    </div>

    <div class="card">
        <h3>🟠 Overstock Risk</h3>
        <p>Products associated with excess inventory exposure.</p>
    </div>

    <div class="card">
        <h3>🔴 Stockout Risk</h3>
        <p>Products exposed to insufficient inventory risk.</p>
    </div>

</div>

<pre><code>
05_risk_scoring.ipynb
</code></pre>


<!-- ================= INVENTORY METRICS ================= -->

<h2>📦 Inventory Intelligence</h2>

<table>

    <tr>
        <th>Metric</th>
        <th>Value</th>
    </tr>

    <tr>
        <td>Products Analysed</td>
        <td>2,030,634</td>
    </tr>

    <tr>
        <td>Healthy Inventory</td>
        <td>583,764</td>
    </tr>

    <tr>
        <td>Stockout Risk</td>
        <td>853,318</td>
    </tr>

    <tr>
        <td>Overstock Risk</td>
        <td>593,552</td>
    </tr>

    <tr>
        <td>Healthy Inventory Rate</td>
        <td>28.7%</td>
    </tr>

</table>


<!-- ================= FINANCIAL ================= -->

<h2>💰 Financial Impact Analysis</h2>

<p>
    Project Foresight extends inventory classification into
    financial decision support by providing indicators related
    to sales exposure and capital locked in inventory.
</p>

<table>

    <tr>
        <th>Financial Metric</th>
        <th>Value</th>
    </tr>

    <tr>
        <td>Sales at Risk</td>
        <td>₹4,505,995</td>
    </tr>

    <tr>
        <td>Locked Capital</td>
        <td>₹9,475,885</td>
    </tr>

</table>


<!-- ================= DASHBOARD ================= -->

<h2>📊 Interactive Streamlit Dashboard</h2>

<p>
    The final analytics layer is implemented as an interactive
    Streamlit dashboard that converts analytical outputs into
    business-friendly visualizations and KPIs.
</p>

<h3>Dashboard Modules</h3>

<ul>
    <li>Sales Analytics</li>
    <li>Demand Forecast</li>
    <li>Inventory Dashboard</li>
    <li>Risk Dashboard</li>
    <li>Product Details</li>
    <li>Executive Summary</li>
</ul>


<h3>📈 Demand Forecast Dashboard</h3>

<ul>
    <li>Forecast units</li>
    <li>Actual units</li>
    <li>Random Forest WAPE</li>
    <li>Forecast improvement</li>
    <li>Actual vs Forecast visualization</li>
    <li>Forecast distribution</li>
    <li>Store filtering</li>
    <li>Year filtering</li>
</ul>


<h3>⚠️ Inventory Risk Dashboard</h3>

<ul>
    <li>Stockout risk</li>
    <li>Overstock risk</li>
    <li>Sales at risk</li>
    <li>Locked capital</li>
    <li>Risk distribution</li>
    <li>SKU count by risk</li>
    <li>Financial impact analysis</li>
</ul>


<h3>📋 Executive Summary</h3>

<p>
    The Executive Summary consolidates the major forecasting,
    inventory and financial KPIs into a single management-oriented
    view.
</p>


<!-- ================= NOTEBOOKS ================= -->

<h2>📚 Notebook Pipeline</h2>

<pre><code>
notebooks/

01_Data_Engineering_Validation.ipynb
        ↓
02_Exploratory_Data_Analysis.ipynb
        ↓
03_Feature_Engineering.ipynb
        ↓
04_Demand_Forecasting.ipynb
        ↓
05_Risk_Scoring.ipynb
        ↓
06_Planning_Dashboard.ipynb
        ↓
07_Deployed_Scoring_Service.ipynb
        ↓
08_Executive_Readout.ipynb
</code></pre>


<!-- ================= STRUCTURE ================= -->

<h2>🗂️ Project Structure</h2>

<pre><code>
Project_Foresight/
│
├── notebooks/
│   ├── 01_Data_Engineering_Validation.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Demand_Forecasting.ipynb
│   ├── 05_Risk_Scoring.ipynb
│   ├── 06_Planning_Dashboard.ipynb
│   ├── 07_Deployed_Scoring_Service.ipynb
│   └── 08_Executive_Readout.ipynb
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   ├── validate_data.py
│   │   ├── transform_data.py
│   │   └── merge_data.py
│   │
│   └── utils/
│       ├── config.py
│       ├── helpers.py
│       ├── logger.py
│       └── pipeline.py
│
├── outputs/
│   ├── decision_summary.csv
│   └── risk_scoring_results.csv
│
├── data/
│   ├── interim/
│   └── processed/
│
├── reports/
├── requirements.txt
├── README.md
├── LICENSE
└── Procfile
</code></pre>


<!-- ================= TECHNOLOGY ================= -->

<h2>🛠️ Technology Stack</h2>

<p>

<span class="badge">Python</span>
<span class="badge">Pandas</span>
<span class="badge">NumPy</span>
<span class="badge">Scikit-learn</span>
<span class="badge">Jupyter</span>
<span class="badge">Plotly</span>
<span class="badge">Streamlit</span>
<span class="badge">Git</span>
<span class="badge">GitHub</span>

</p>

<h3>Analytics & Data Engineering</h3>

<ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Data validation</li>
    <li>Data transformation</li>
    <li>Feature engineering</li>
</ul>

<h3>Machine Learning</h3>

<ul>
    <li>Random Forest</li>
    <li>Demand forecasting</li>
    <li>Risk scoring</li>
    <li>WAPE model evaluation</li>
</ul>

<h3>Visualization & BI</h3>

<ul>
    <li>Plotly</li>
    <li>Plotly Express</li>
    <li>Streamlit</li>
</ul>


<!-- ================= WAPE ================= -->

<h2>📏 Forecast Evaluation</h2>

<p>
    Weighted Absolute Percentage Error (WAPE) is used to evaluate
    forecasting performance.
</p>

<pre><code>
              Σ |Actual - Forecast|
WAPE = -------------------------------
                    Σ |Actual|
</code></pre>

<p>
    Lower WAPE indicates better forecasting performance.
</p>

<p>
    The current dashboard reports a Random Forest WAPE of
    <strong>0.5905</strong>.
</p>


<!-- ================= BUSINESS INSIGHTS ================= -->

<h2>💡 Key Business Insights</h2>

<div class="success">

    <strong>Inventory Health:</strong>

    <p>
        28.7% of analysed products are currently classified
        as healthy inventory.
    </p>

</div>

<div class="danger">

    <strong>Stockout Risk:</strong>

    <p>
        853,318 products are classified under stockout risk,
        making it the largest risk category in the current
        dashboard output.
    </p>

</div>

<div class="warning">

    <strong>Overstock Risk:</strong>

    <p>
        593,552 products are classified under overstock risk.
    </p>

</div>

<p>
    Overall, 1,446,870 products are identified as being
    at risk across the stockout and overstock categories.
</p>


<!-- ================= DECISION SUPPORT ================= -->

<h2>🎯 Decision Intelligence</h2>

<pre><code>
What happened?
      ↓
Historical Sales Analytics
      ↓
What is likely to happen?
      ↓
Demand Forecasting
      ↓
Where is the inventory problem?
      ↓
Risk Scoring
      ↓
What is the financial impact?
      ↓
Sales-at-Risk / Locked-Capital Analysis
      ↓
What should be prioritized?
      ↓
Interactive Decision Dashboard
</code></pre>


<!-- ================= RUN ================= -->

<h2>▶️ Running the Project Locally</h2>

<h3>1. Clone the Repository</h3>

<pre><code>
git clone https://github.com/PragzzX/Project_Foresight.git
cd Project_Foresight
</code></pre>

<h3>2. Create a Virtual Environment</h3>

<pre><code>
python -m venv .venv
</code></pre>

<h3>3. Activate the Environment</h3>

<pre><code>
.venv\Scripts\activate
</code></pre>

<h3>4. Install Dependencies</h3>

<pre><code>
pip install -r requirements.txt
</code></pre>

<h3>5. Start the Dashboard</h3>

<pre><code>
streamlit run dashboard/app.py
</code></pre>


<!-- ================= FUTURE ================= -->

<h2>🚀 Future Enhancements</h2>

<ul>
    <li>Automated model retraining</li>
    <li>Real-time inventory integration</li>
    <li>Automated data pipelines</li>
    <li>Product-level reorder recommendations</li>
    <li>Safety-stock optimization</li>
    <li>Forecast confidence intervals</li>
    <li>Model monitoring</li>
    <li>Data-quality monitoring</li>
    <li>Automated high-risk inventory alerts</li>
    <li>Cloud data warehouse integration</li>
</ul>


<!-- ================= AUTHOR ================= -->

<h2>👩‍💻 Author</h2>

<div class="card">

    <h3>L Pragna</h3>

    <p>
        <strong>Project:</strong>
        Project Foresight
    </p>

    <p>
        <strong>Focus:</strong>
        Data Analytics • Machine Learning • Demand Forecasting •
        Inventory Intelligence
    </p>

    <p>
        <strong>GitHub Repository:</strong><br>

        <a href="https://github.com/PragzzX/Project_Foresight"
           target="_blank">
            github.com/PragzzX/Project_Foresight
        </a>
    </p>

</div>


<!-- ================= SUMMARY ================= -->

<h2>📄 Project Summary</h2>

<p>
    <strong>Project Foresight</strong> demonstrates an end-to-end
    approach to solving a retail analytics problem using data
    engineering, exploratory analytics, machine learning,
    demand forecasting, inventory risk scoring and interactive
    business intelligence.
</p>

<p>
    The platform connects:
</p>

<pre><code>
Data
  ↓
Features
  ↓
Forecasts
  ↓
Risk Scores
  ↓
Financial Impact
  ↓
Business Decisions
</code></pre>


<!-- ================= SKILLS ================= -->

<h2>⭐ Skills Demonstrated</h2>

<p>

<span class="badge">Python</span>
<span class="badge">Data Cleaning</span>
<span class="badge">Data Validation</span>
<span class="badge">EDA</span>
<span class="badge">Feature Engineering</span>
<span class="badge">Machine Learning</span>
<span class="badge">Random Forest</span>
<span class="badge">Demand Forecasting</span>
<span class="badge">WAPE</span>
<span class="badge">Risk Scoring</span>
<span class="badge">Business KPIs</span>
<span class="badge">Financial Analysis</span>
<span class="badge">Plotly</span>
<span class="badge">Streamlit</span>
<span class="badge">Jupyter</span>
<span class="badge">Git</span>
<span class="badge">GitHub</span>
<span class="badge">Dashboard Development</span>
<span class="badge">Decision Intelligence</span>

</p>


<!-- ================= FOOTER ================= -->

<div class="footer">

    <p>
        <strong>Project Foresight</strong> —
        AI-Powered Retail Demand Forecasting &
        Inventory Risk Intelligence Platform
    </p>

    <p>
        Developed by <strong>L Pragna</strong>
    </p>

</div>

</body>
</html>
