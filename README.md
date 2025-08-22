FinOps Dashboard for Cloud Cost Visibility (Free Tier Usage Tracker)

Objective:
Monitor and visualize cloud resource usage to detect free-tier limit breaches before billing starts.

Features

Fetch daily resource usage from GCP Billing API (or AWS Cost Explorer API for AWS).

Store usage data in SQLite for easy querying and persistence.

Visualize trends and usage statistics in Grafana dashboards.

Flag “at-risk” services to prevent unexpected costs.

Generate weekly usage reports.

Tech Stack

Python – Fetch and parse API data, store in SQLite.

SQLite – Store usage data and risk flags.

Grafana – Visualize usage trends and service alerts.

APIs – GCP Billing API / AWS Cost Explorer API.

Setup

Enable APIs

GCP: Cloud Billing API, Cloud Resource Manager API.

AWS: Cost Explorer API (if using AWS).

Service Account (GCP)

Create a service account with Billing Account Viewer role.

Download JSON key and place it as service_account.json 

Python Environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Run Data Fetch Script

python fetch_usage.py


Visualize in Grafana

Add SQLite data source pointing to usage_data.db.

Import dashboards and configure panels to show usage and risk alerts.

Example Database Structure
Usage Table
service	usage	unit	timestamp
compute_engine	20.0	hours	2025-08-22 14:27:30
storage	5.0	GB	2025-08-22 14:27:30
Risks Table
service	message	timestamp
compute_engine	Compute Engine nearing free tier!	2025-08-22 14:27:30
storage	Storage usage approaching free tier	2025-08-22 14:27:30
