import csv
import json

def read_users_csv():
    with open("data/user.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_products_json():
    with open("data/product.json") as file:
        return json.load(file)