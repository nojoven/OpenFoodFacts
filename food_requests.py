import requests as reqs


class Collector:

    def __init__(self):
        self.params = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': 'category', 'sort_by': 'unique_scans_n', 'page_size': 1000, 'json': 1}
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def get_products_by_category(self, category):
        results = []
        self.params["tag_0"] = category
        req = reqs.get(self.url, self.params)
        data = req.json()
        products = data["products"]
        for product in products:
            try:
                product_data = {
                    "stores_tags": product["stores_tags"],
                    "brands": product["brands"],
                    "product_name": product["product_name"],
                    "nutrition_grade_fr": product["nutrition_grade_fr"],
                    "quantity": product["quantity"]
                }
            except KeyError:
                continue
            results.append(product_data)
        return results




