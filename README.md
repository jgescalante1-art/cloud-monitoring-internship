# Cloud Monitoring - Week 10

## Stack
- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Python Flask + prometheus_client

## How to Run
```bash
docker-compose up -d
source venv/bin/activate
python3 app.py
```

## Services
| Service | URL |
|---|---|
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| cAdvisor | http://localhost:8080 |
| Flask App | http://localhost:5001 |
