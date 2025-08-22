import os
import yaml
from gcp_client import GCPClient
from database import Database
from logic.risk_rules import check_risks

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Initialize GCP Client
gcp = GCPClient(
    project_id=os.getenv("GCP_PROJECT_ID"),
    billing_account_id=os.getenv("GCP_BILLING_ACCOUNT_ID"),
    key_file=config["gcp"]["key_file"]
)

# Fetch usage data
usage_data = gcp.get_usage_data()

# Store in SQLite
db = Database("usage_data.db")
db.save_usage(usage_data)

# Run risk checks
risks = check_risks(usage_data, config["limits"])
db.save_risks(risks)

print("✅ Data fetched, stored, and risk checks completed.")
