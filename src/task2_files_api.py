"""Task 2: CSV/JSON file handling and REST API access."""

import csv
import json
from pathlib import Path

import requests
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_and_write_employees():
    with (DATA / "employees.csv").open("r", newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    with (DATA / "employees.json").open("w", encoding="utf-8") as target:
        json.dump(rows, target, indent=2)

    high_earners = [row for row in rows if int(row["salary"]) > 50000]
    with (DATA / "high_earners.csv").open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(high_earners)

    print(f"Rows read: {len(rows)} | High earners: {len(high_earners)}")
    return rows


def fetch_users():
    load_dotenv(ROOT / ".env")
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        response = requests.get(f"{base_url}/users", timeout=5)
        response.raise_for_status()
        users = response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
        users = []
    except requests.exceptions.ConnectionError:
        print("Connection error")
        users = []

    for user in users[:3]:
        print(f"{user['id']} - {user['name']} - {user['email']}")

    try:
        missing = requests.get(f"{base_url}/users/9999", timeout=5)
        if missing.status_code == 404:
            print("/users/9999 -> 404 Not found")
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
        print(f"Request failed: {exc}")

    first_result = users[0] if users else {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz",
        "address": {"geo": {"lat": "-37.3159"}},
    }
    nested_lat = first_result.get("address", {}).get("geo", {}).get("lat", "N/A")
    output = {"id": first_result["id"], "name": first_result["name"],
              "email": first_result["email"], "nested_lat": nested_lat}
    with (DATA / "users.json").open("w", encoding="utf-8") as target:
        json.dump(output, target, indent=2)


if __name__ == "__main__":
    read_and_write_employees()
    fetch_users()
