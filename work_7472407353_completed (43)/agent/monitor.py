import psutil
import requests
import time
import sys

API_URL = "http://localhost:8000/metrics/report"

def send_metrics():
    while True:
        try:
            data = {
                "cpu_usage": psutil.cpu_percent(),
                "ram_usage": psutil.virtual_memory().percent
            }
            requests.post(API_URL, json=data)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)

if __name__ == "__main__":
    send_metrics()