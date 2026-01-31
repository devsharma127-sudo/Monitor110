import csv
import json
from datetime import datetime

INPUT_FILE = "yahoo_finance_data.csv"
OUTPUT_FILE = "arranged_data.json"

arranged_data = []

with open(INPUT_FILE, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        arranged_item = {
            "source": row.get("source", "Unknown"),
            "headline": row.get("title", "").strip(),
            "text": row.get("summary", "").strip(),
            "timestamp": row.get("published", str(datetime.now()))
        }
        arranged_data.append(arranged_item)

with open(OUTPUT_FILE, "w", encoding="utf-8") as json_file:
    json.dump(arranged_data, json_file, indent=4, ensure_ascii=False)

print("Arranging done! File saved as arranged_data.json")