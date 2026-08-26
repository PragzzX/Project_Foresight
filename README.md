<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project FORESIGHT | AI-Powered Demand & Inventory Intelligence</title>
    
    <!-- Modern Inter & JetBrains Mono Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --primary-light: #60a5fa;
            --accent: #0ea5e9;
            --bg-body: #0b0f19;
            --bg-card: #111827;
            --bg-card-hover: #1f2937;
            --border-color: #1f2937;
            --border-focus: #374151;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --text-dim: #6b7280;
            --danger: #ef4444;
            --danger-bg: rgba(239, 68, 68, 0.12);
            --warning: #f59e0b;
            --warning-bg: rgba(245, 158, 11, 0.12);
            --success: #10b981;
            --success-bg: rgba(16, 185, 129, 0.12);
            --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', Consolas, monospace;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-main);
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.65;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            max-width: 1180px;
            width: 100%;
        }

        /* Hero Banner */
        .hero {
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(14, 165, 233, 0.05) 100%);
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 20px;
            padding: 50px 40px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
            margin-bottom: 40px;
        }

        .hero::before {
            content: "";
            position: absolute;
            top: -50%;
            right: -20%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(37, 99, 235, 0.25) 0%, transparent 70%);
            pointer-events: none;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            border-radius: 30px;
            background: rgba(37, 99, 235, 0.15);
            border: 1px solid rgba(96, 165, 250, 0.3);
            color: var(--primary-light);
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: 42px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 12px;
            letter-spacing: -0.02em;
        }

        .hero p.lead {
            font-size: 18px;
            color: var(--text-muted);
            max-width: 800px;
            margin-bottom: 25px;
        }

        .hero-links {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .btn-primary {
            background: var(--primary);
            color: #ffffff;
            border: 1px solid var(--primary-light);
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
        }

        .btn-primary:hover {
            background: var(--primary-dark);
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: var(--bg-card);
            color: var(--text-main);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: var(--bg-card-hover);
            border-color: var(--text-muted);
            transform: translateY(-2px);
        }

        /* Section Typography */
        h2.section-title {
            font-size: 24px;
            font-weight: 700;
            color: #ffffff;
            margin: 50px 0 20px 0;
            display: flex;
            align-items: center;
            gap: 12px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
        }

        h3.subsection-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--primary-light);
            margin: 25px 0 12px 0;
        }

        p {
            color: var(--text-muted);
            margin-bottom: 16px;
            font-size: 15px;
        }

        /* Metric Grid Cards */
        .grid-4 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            margin: 24px 0;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 20px;
            margin: 24px 0;
        }

        .card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            transition: transform 0.2s, border-color 0.2s;
            position: relative;
        }

        .card:hover {
            transform: translateY(-3px);
            border-color: var(--border-focus);
        }

        .card-label {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }

        .card-value {
            font-size: 30px;
            font-weight: 800;
            color: #ffffff;
            font-family: var(--font-mono);
            margin-bottom: 6px;
        }

        .card-subtext {
            font-size: 13px;
            color: var(--text-muted);
        }

        /* Status Panels */
        .status-panel {
            border-radius: 12px;
            padding: 20px;
            margin: 16px 0;
            border-left: 4px solid transparent;
        }

        .status-danger {
            background: var(--danger-bg);
            border-color: var(--danger);
        }

        .status-warning {
            background: var(--warning-bg);
            border-color: var(--warning);
        }

        .status-success {
            background: var(--success-bg);
            border-color: var(--success);
        }

        .status-panel h4 {
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .status-danger h4 { color: var(--danger); }
        .status-warning h4 { color: var(--warning); }
        .status-success h4 { color: var(--success); }

        .status-panel ul {
            padding-left: 20px;
            color: var(--text-main);
            font-size: 14px;
        }

        .status-panel ul li {
            margin-bottom: 6px;
        }

        /* Visual Screenshot Wrapper Slots */
        .screenshot-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            overflow: hidden;
            margin: 24px 0;
        }

        .screenshot-img-container {
            width: 100%;
            max-height: 480px;
            overflow: hidden;
            background: #000000;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .screenshot-img-container img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }

        .screenshot-caption {
            padding: 16px 20px;
            border-top: 1px solid var(--border-color);
            background: rgba(0, 0, 0, 0.2);
            font-size: 13.5px;
            color: var(--text-muted);
            font-family: var(--font-mono);
        }

        .screenshot-caption strong {
            color: var(--primary-light);
        }

        /* Clean Tables */
        .table-responsive {
            overflow-x: auto;
            margin: 20px 0;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 14px;
        }

        th {
            background: #1e293b;
            color: var(--text-main);
            padding: 14px 18px;
            font-weight: 600;
            border-bottom: 1px solid var(--border-color);
        }

        td {
            padding: 14px 18px;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-muted);
        }

        tr:last-child td {
            border-bottom: none;
        }

        tr:hover td {
            background: rgba(255, 255, 255, 0.02);
            color: var(--text-main);
        }

        /* Code and Pre blocks */
        pre {
            background: #090d16;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 13.5px;
            color: #38bdf8;
            line-height: 1.5;
            margin: 16px 0;
        }

        code {
            font-family: var(--font-mono);
            color: var(--primary-light);
            background: rgba(37, 99, 235, 0.1);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 13.5px;
        }

        /* Tags */
        .badge-list {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 16px 0;
        }

        .tech-badge {
            font-family: var(--font-mono);
            font-size: 12px;
            font-weight: 500;
            padding: 4px 10px;
            border-radius: 6px;
            background: #1e293b;
            color: #93c5fd;
            border: 1px solid #334155;
        }

        /* Footer */
        .footer {
            margin-top: 80px;
            padding-top: 30px;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--text-dim);
            font-size: 13.5px;
            flex-wrap: wrap;
            gap: 15px;
        }

        .footer a {
            color: var(--text-muted);
            text-decoration: none;
        }

        .footer a:hover {
            color: var(--primary-light);
        }
    </style>
</head>
<body>

<div class="container">

    <!-- ================= HERO ================= -->
    <header class="hero">
        <div class="hero-badge">AI Demand & Inventory Intelligence</div>
        <h1>Project FORESIGHT</h1>
        <p class="lead">
            An enterprise-scale retail forecasting engine and inventory decision platform. Transforms over 58 million daily transaction records into weekly demand forecasts, risk scoring classifications, and actionable working capital controls.
        </p>
        <div class="hero-links">
            <a href="https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/" target="_blank" class="btn btn-primary">
                🚀 Open Live Streamlit App
            </a>
            <a href="https://github.com/PragzzX/Project_Foresight" target="_blank" class="btn btn-secondary">
                📂 GitHub Repository
            </a>
        </div>
    </header>

    <!-- ================= EXECUTIVE KPI SUMMARY ================= -->
    <section>
        <h2 class="section-title">📊 Executive Scorecard & Headline Results</h2>
        <div class="grid-4">
            <div class="card">
                <div class="card-label">Random Forest WAPE</div>
                <div class="card-value" style="color: #38bdf8;">59.05%</div>
                <div class="card-subtext">vs. 71.41% Seasonal Naive baseline</div>
            </div>
            <div class="card">
                <div class="card-label">Accuracy Improvement</div>
                <div class="card-value" style="color: #10b981;">+17.3%</div>
                <div class="card-subtext">12.36 pp net error reduction</div>
            </div>
            <div class="card">
                <div class="card-label">Stockout Sales at Risk</div>
                <div class="card-value" style="color: #ef4444;">₹4.50M</div>
                <div class="card-subtext">853,318 SKU-weeks requiring reorders</div>
            </div>
            <div class="card">
                <div class="card-label">Locked Capital (Overstock)</div>
                <div class="card-value" style="color: #f59e0b;">₹9.47M</div>
                <div class="card-subtext">593,552 SKU-weeks requiring markdowns</div>
            </div>
        </div>

        <!-- Integrated Screenshot Slot: Executive Summary -->
        <div class="screenshot-card">
            <div class="screenshot-img-container">
                <img src="1000051778.jpg" alt="Executive Summary Dashboard">
            </div>
            <div class="screenshot-caption">
                <strong>Figure 1.1:</strong> Executive Summary Dashboard synthesizing actual vs forecast units (5,223,487 vs 5,667,654), model performance comparison, and portfolio risk distributions.
            </div>
        </div>
    </section>

    <!-- ================= PROBLEM STATEMENT ================= -->
    <section>
        <h2 class="section-title">🎯 Operational Challenges & Business Value</h2>
        <p>
            Retail inventory planning balances two costly conditions: under-forecasting that causes stockouts, and over-forecasting that ties up working capital. Project FORESIGHT bridges the gap between predictive ML models and inventory decision-making.
        </p>

        <div class="grid-2">
            <div class="status-panel status-danger">
                <h4>🔴 Under-Forecasting & Stockout Exposure</h4>
                <ul>
                    <li>Loss of top-line revenue and customer goodwill.</li>
                    <li>Unfulfilled demand across high-velocity items.</li>
                    <li>853,318 SKU-weeks flagged with high stockout probability.</li>
                    <li><strong>Financial Impact:</strong> ₹4,505,995 in sales at risk.</li>
                </ul>
            </div>

            <div class="status-panel status-warning">
                <h4>🟠 Over-Forecasting & Excess Working Capital</h4>
                <ul>
                    <li>Excess storage and warehouse holding costs.</li>
                    <li>Forced markdown cycles and margin degradation.</li>
                    <li>593,552 SKU-weeks classified as overstocked.</li>
                    <li><strong>Financial Impact:</strong> ₹9,475,885 in locked capital.</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- ================= DATA ARCHITECTURE & CHUNKING ================= -->
    <section>
        <h2 class="section-title">🏗️ Data Engineering & 64-Chunk Architecture</h2>
        <p>
            Standard pandas workflows fail on the 58.3M record M5 dataset due to memory limits. FORESIGHT implements a chunked transformation pipeline that creates weekly SKU-store modeling records stored as compressed Parquet files.
        </p>

        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Pipeline Stage</th>
                        <th>Record Grain</th>
                        <th>Volume / Dimensions</th>
                        <th>Processing Strategy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Daily Sales Matrix</strong></td>
                        <td>SKU × Store × Day</td>
                        <td>30,490 × 1,919 matrix</td>
                        <td>Wide unpivot via 64 memory-bounded chunks</td>
                    </tr>
                    <tr>
                        <td><strong>Calendar Context</strong></td>
                        <td>Daily Timeline</td>
                        <td>1,969 dates × 14 attributes</td>
                        <td>SNAP indicators, events, and weekend flags</td>
                    </tr>
                    <tr>
                        <td><strong>Sell Prices</strong></td>
                        <td>SKU × Store × Week</td>
                        <td>6,841,121 records × 4 attributes</td>
                        <td>Store-level pricing joins with null checks</td>
                    </tr>
                    <tr>
                        <td><strong>Merged Analytical Master</strong></td>
                        <td>Long Transactional</td>
                        <td>58,327,370 rows × 22 columns</td>
                        <td>Snappy-compressed Parquet storage</td>
                    </tr>
                    <tr>
                        <td><strong>Weekly Modeling Grain</strong></td>
                        <td>SKU × Store × Week</td>
                        <td>10,153,170 rows</td>
                        <td>Lag and shifted rolling feature extraction</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- ================= FORECASTING RESULTS ================= -->
    <section>
        <h2 class="section-title">🤖 Model Performance & Feature Importance</h2>
        <p>
            Models were trained using an 80/20 chronological train/test split (8,122,536 training rows / 2,030,634 test rows) to eliminate future data leakage. The Random Forest model achieved a 59.05% WAPE, outperforming the Seasonal Naive baseline (71.41%).
        </p>

        <!-- Integrated Screenshot Slot: Forecast Time Series -->
        <div class="screenshot-card">
            <div class="screenshot-img-container">
                <img src="1000051777.jpg" alt="Demand Forecast Dashboard">
            </div>
            <div class="screenshot-caption">
                <strong>Figure 2.1:</strong> Demand Forecast Dashboard depicting actual vs predicted unit sales across historical test horizons with store and year filtering.
            </div>
        </div>

        <h3 class="subsection-title">Feature Importance Analysis</h3>
        <p>
            Feature importance analysis demonstrates that recent four-week demand levels serve as the dominant predictive signal:
        </p>

        <pre><code>rolling_mean_4  ████████████████████████████████████████ 70.51%
lag_1           ███████ 13.45%
is_weekend      ███ 6.41%
rolling_std_4   ██ 3.11%
lag_8           █ 1.67%
lag_2           █ 1.50%
sell_price      █ 1.26%
lag_4           █ 1.25%
has_event       ▎ 0.52%
has_snap        ▎ 0.31%</code></pre>
    </section>

    <!-- ================= INVENTORY INTELLIGENCE ================= -->
    <section>
        <h2 class="section-title">⚠️ Inventory Intelligence & Risk Quantification</h2>
        <p>
            The risk engine translates weekly unit forecasts into operational inventory states using deterministic replenishment logic:
        </p>

        <div class="grid-2">
            <!-- Integrated Screenshot Slot: Snapshot -->
            <div class="screenshot-card">
                <div class="screenshot-img-container">
                    <img src="1000051776.jpg" alt="Intelligence Snapshot">
                </div>
                <div class="screenshot-caption">
                    <strong>Figure 3.1:</strong> Portfolio Health Index (28.7% Healthy) and dominant stockout exposure breakdown.
                </div>
            </div>

            <!-- Integrated Screenshot Slot: Risk Details -->
            <div class="screenshot-card">
                <div class="screenshot-img-container">
                    <img src="1000051779.jpg" alt="Inventory Risk Dashboard">
                </div>
                <div class="screenshot-caption">
                    <strong>Figure 3.2:</strong> Inventory Risk Dashboard quantifying ₹4.50M in sales at risk and ₹9.47M in locked capital.
                </div>
            </div>
        </div>

        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Risk Priority</th>
                        <th>Classification Criteria</th>
                        <th>Evaluated SKUs</th>
                        <th>Share</th>
                        <th>Financial Impact</th>
                        <th>Operational Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><span style="color: #ef4444; font-weight:700;">Stockout (High)</span></td>
                        <td><code>Gap &lt; 0</code></td>
                        <td>853,318</td>
                        <td>42.0%</td>
                        <td>₹4,505,995 Sales at Risk</td>
                        <td>Trigger urgent purchase reorder</td>
                    </tr>
                    <tr>
                        <td><span style="color: #f59e0b; font-weight:700;">Overstock (Medium)</span></td>
                        <td><code>Gap &gt; 0.50 × Forecast</code></td>
                        <td>593,552</td>
                        <td>29.2%</td>
                        <td>₹9,475,885 Locked Capital</td>
                        <td>Halt POs & trigger markdowns</td>
                    </tr>
                    <tr>
                        <td><span style="color: #10b981; font-weight:700;">Healthy (Low)</span></td>
                        <td><code>0 ≤ Gap ≤ 0.50 × Forecast</code></td>
                        <td>583,764</td>
                        <td>28.7%</td>
                        <td>₹0 Excess Exposure</td>
                        <td>Maintain current replenishment</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- ================= RUNNING LOCALLY ================= -->
    <section>
        <h2 class="section-title">▶️ Setup and Local Execution</h2>
        <pre><code># 1. Clone the project repository
git clone https://github.com/PragzzX/Project_Foresight.git
cd Project_Foresight

# 2. Configure virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Streamlit multi-page dashboard
streamlit run dashboard/app.py</code></pre>
    </section>

    <!-- ================= TECH STACK BADGES ================= -->
    <section>
        <h2 class="section-title">🛠️ Core Technologies & Tools</h2>
        <div class="badge-list">
            <span class="tech-badge">Python 3.10+</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">NumPy</span>
            <span class="tech-badge">PyArrow</span>
            <span class="tech-badge">Scikit-Learn</span>
            <span class="tech-badge">Random Forest</span>
            <span class="tech-badge">Joblib</span>
            <span class="tech-badge">Streamlit</span>
            <span class="tech-badge">Power BI</span>
            <span class="tech-badge">Parquet</span>
            <span class="tech-badge">Plotly</span>
        </div>
    </section>

    <!-- ================= FOOTER ================= -->
    <footer class="footer">
        <div>
            <strong>Project FORESIGHT</strong> — Developed by <strong>L Pragna</strong>
        </div>
        <div>
            <a href="https://github.com/PragzzX/Project_Foresight" target="_blank">GitHub Repository</a> • 
            <a href="https://pragzzx-project-foresight-dashboardapp-jaxeze.streamlit.app/" target="_blank">Live Application</a>
        </div>
    </footer>

</div>

</body>
</html>
