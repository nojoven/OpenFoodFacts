from food_requests import Collector
from modeles.category import Categories
from modeles.favorite import Favorites
from modeles.product import Product
from modules.database_service import DatabaseService


Product.create_table()
Categories.create_table()
Favorites.create_table()

collector = Collector()
list_of_categories = ('soup', 'pizza', 'salad', 'cake', 'cheese')

for category in list_of_categories:
    category_entry = {"Name": category}
    DatabaseService.fill_categories_table(category_entry)


for category in list_of_categories:
    food_returned = collector.get_products_by_category(category)
    DatabaseService.fill_products_table(food_returned)

