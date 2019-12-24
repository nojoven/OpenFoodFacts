from json import JSONDecodeError

import requests as reqs
import peewee
from modeles.product import Product


class Collector:

    def __init__(self):
        self.params = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': 'category', 'sort_by': 'unique_scans_n', 'page_size': 1000, 'json': 1}
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def get_products_by_category(self, category):
        results = []
        products = []
        try:
            self.params["tag_0"] = category
            req = reqs.get(self.url, self.params)
            data = req.json()
            products = data["products"]

        except JSONDecodeError:
            pass
        for product in products:
            try:
                if not product["stores_tags"] or not product["quantity"]:
                    continue
                product_data = {
                    "Stores": str(product["stores_tags"])[1:-1],
                    "Brands": product["brands"],
                    "ProductName": product["product_name"],
                    "Nutrigrade": product["nutrition_grade_fr"],
                    "Category": category,
                    "Quantity": product["quantity"]
                }
            except KeyError:
                continue
            results.append(product_data)
        return results




