import requests
import json
import csv


csv_file = "customer.csv"
api_url = "placeholder"
processed_data = []

#fetch
try:
    response = requests.get(api_url)
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()

#process
for user in data:
    processed_data.append({
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"]
    })


#csv output
try:
    with open(csv_file, "w",newline="")
        writer = csv.DictWriter(csv_file, fieldnames=processed_data[0].keys())
        writer.writeheader()
        writer.writerows(processed_data)
        print(f"Data saved to {csv_file}")
except IOError as e:
    print(f"Error writing CSV: {e}")