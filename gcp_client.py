import os
from google.cloud import billing

class GCPClient:
    def __init__(self, project_id, billing_account_id, key_file):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file
        self.project_id = project_id
        self.billing_account_id = billing_account_id

    def get_usage_data(self):
        # Mock function: Replace with real API calls
        usage_data = [
            {"service": "bigquery", "usage": 0.8, "unit": "TB"},
            {"service": "storage", "usage": 4, "unit": "GB"},
            {"service": "compute_engine", "usage": 100, "unit": "hours"}
        ]
        return usage_data
