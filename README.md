# FinOps Dashboard for Cloud Cost Visibility (Free Tier Usage Tracker)

## Objective
Monitor and visualize cloud resource usage to detect free-tier limit breaches **before billing starts**, helping prevent unexpected cloud costs by proactively flagging at-risk services.

## Features
- Fetch daily resource usage from:
  - **GCP**: Cloud Billing API  
  - **AWS**: Cost Explorer API (optional)  
- Store usage data in **SQLite** for easy querying and persistence.  
- Visualize trends and usage statistics in **Grafana dashboards**.  
- Flag “at-risk” services approaching free-tier limits.  
- Generate weekly usage reports automatically.

## Tech Stack
- **Python** – Fetch and parse API data, store in SQLite.  
- **SQLite** – Store usage data and risk flags.  
- **Grafana** – Visualize usage trends and service alerts.  
- **APIs** – GCP Billing API / AWS Cost Explorer API.  

## Setup

### Enable APIs
**GCP**:
- Cloud Billing API  
- Cloud Resource Manager API  

**AWS** (if using AWS):
- Cost Explorer API  

### GCP Service Account
1. Create a service account with **Billing Account Viewer** role.  
2. Download the JSON key and save it as `service_account.json`.

### Python Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
Run Data Fetch Script
bash
Copy
Edit
python fetch_usage.py
Database Structure
Usage Table
service	usage	unit	timestamp
compute_engine	20.0	hours	2025-08-22 14:27:30
storage	5.0	GB	2025-08-22 14:27:30

Risks Table
service	message	timestamp
compute_engine	Compute Engine nearing free tier!	2025-08-22 14:27:30
storage	Storage usage approaching free tier	2025-08-22 14:27:30

Grafana Configuration
Add SQLite Data Source
Open Grafana → Configuration → Data Sources → Add data source

Select SQLite

If the plugin is not installed:

bash
Copy
Edit
grafana-cli plugins install fr-ser-sqlite-datasource
Then restart Grafana.

Set Path to your SQLite database:

pgsql
Copy
Edit
path/to/usage_data.db
Click Save & Test – it should say Data source is working

Import Dashboards
Create or import dashboards with panels showing:

Daily usage trends per service

Usage vs. free-tier limits

At-risk services alerts

Configure Panels
Graph Panel: Plot usage over timestamp for each service

Stat Panel: Show current usage and highlight services approaching limits

Alert Panel: Trigger alerts if usage crosses defined free-tier thresholds

Optional: Weekly Reports
Set up a Grafana alert or scheduled report to email usage summaries weekly.

Step-by-Step Grafana Setup Guide
Install Grafana

Download from Grafana Downloads

Start Grafana (http://localhost:3000)

Default login: admin / admin

Add SQLite Data Source

Configuration → Data Sources → Add Data Source → SQLite

Path: usage_data.db

Click Save & Test

Create a Dashboard

Dashboards → New Dashboard → Add New Panel

Select SQLite as data source

Graph Panel example query:

sql
Copy
Edit
SELECT timestamp, usage FROM Usage WHERE service='compute_engine' ORDER BY timestamp
Stat Panel: show latest usage

Alert Panel: set thresholds for free-tier limits

Import Prebuilt Dashboard (Optional)

Dashboards → Import → Paste JSON / Upload file

Select SQLite data source → Import

Set Up Weekly Reports (Optional)

Alerting → Notification channels → Add Email/Slack

Dashboard → Share → Schedule Report → Choose frequency

This project enables full visibility into cloud free-tier usage, preventing unexpected billing and helping optimize your cloud resources effectively.
