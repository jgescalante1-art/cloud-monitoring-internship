from flask import Flask
from prometheus_client import start_http_server, Counter, Gauge
import pandas as pd

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total App Requests')
CLOUD_COST = Gauge('cloud_estimated_cost', 'Estimated Cloud Cost')

def calculate_cost():
    data = {
        "Service": ["Compute", "Storage", "Network"],
        "Usage": [120, 500, 80],
        "Cost_per_unit": [0.05, 0.02, 0.01]
    }
    import pandas as pd
    df = pd.DataFrame(data)
    df["Total_Cost"] = df["Usage"] * df["Cost_per_unit"]
    return df["Total_Cost"].sum()

# Set the cost metric
CLOUD_COST.set(calculate_cost())

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Cloud Service Running"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5001)
