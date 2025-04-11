import json
import os

filename = "tracked_products.json"

def load_data():
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
