import requests
import time
import random

API_URL = "http://127.0.0.1:8000/ingest"
components = ["auth-service", "payment-gateway", "inventory-db"]

def send_signals():
    print(f"🚀 Starting Simulator...")
    for i in range(5):
        # This dictionary must match the Signal class in models.py exactly!
        data = {
            "component_id": random.choice(components),
            "signal_type": "ERROR",
            "severity": random.randint(1, 5),
            "timestamp": "2026-05-06T12:00:00"
        }
        
        try:
            response = requests.post(API_URL, json=data)
            print(f"[{i+1}] Sent {data['component_id']} | Status: {response.status_code}")
        except Exception as e:
            print(f"❌ Failed: {e}")
        time.sleep(1)

if __name__ == "__main__":
    send_signals()