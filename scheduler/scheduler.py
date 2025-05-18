import requests
import schedule
import time
from datetime import datetime

DISCOVERY_URL = "http://localhost:8000/discovery"
PARSER_URL = "http://localhost:8000/parse"

def run_discovery():
    print(f"[{datetime.now()}] Checking for URLs")
    try:
        res = requests.post(DISCOVERY_URL)
        print(f"Discovery results: {res.status_code} {res.text}")
    except Exception as e:
        print(f"Error: {e}")

def run_parser():
    print(f"[{datetime.now()}] Checking for data")
    try:
        res = requests.post(PARSER_URL)
        print(f"Parsing results: {res.status_code} {res.text}")
    except Exception as e:
        print(f"Error: {e}")

def job():
    run_discovery()
    run_parser()

schedule.every().minute.do(job)

if __name__ == "__main__":
    print("Starting crawling")
    job()
    while True:
        schedule.run_pending()
        time.sleep(60)