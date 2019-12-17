from food_requests import Collector
from modules.database_service import DatabaseService

collector = Collector()
list_of_categories = ('soup', 'pizza', 'salad', 'cake', 'cheese')
list_of_products = []

soups_returned = collector.get_products_by_category(list_of_categories[0])
list_of_products.append(soups_returned)
# print(soups_returned)
# pizzas_returned = collector.get_products_by_category(list_of_categories[1])
# print(pizzas_returned)
# salads_returned = collector.get_products_by_category(list_of_categories[2])
# print(salads_returned)
# cakes_returned = collector.get_products_by_category(list_of_categories[3])
# print(cakes_returned)
# cheeses_returned = collector.get_products_by_category(list_of_categories[4])
# print(cheeses_returned)

db = DatabaseService.get_instance()
db.connect_to_mysql("root", "Hamzamal89", "127.0.0.1", "purbeurre")
print(db.is_connected())

#db.insert_category(list_of_categories)


