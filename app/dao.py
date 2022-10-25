import json
import os
from app import sale_app


def load_categories():
    with open("%s/data/categories.json" % sale_app.root_path, encoding='utf-8') as f:
        return json.load(f)


def load_products(category_id=None):
    with open("%s/data/products.json" % sale_app.root_path, encoding='utf-8') as f:
        products = json.load(f)
    if category_id:
        products = [p for p in products if p["category_id"] == int(category_id)]
    return products
