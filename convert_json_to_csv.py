import json
import csv

# Load the JSON response
with open("data/celo_balances.json", "r") as f:
    data = json.load(f)

rows = data["result"]["rows"]
columns = data["result"]["metadata"]["column_names"]

# Write to CSV
with open("data/celo_balances.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)

print("✅ CSV saved to data/celo_balances.csv")
