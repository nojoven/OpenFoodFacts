"""

Creating and populating the database

This file is used to :

    - Create the MySQL tables "Categories", "Products" and  "Favorites"
    - Populate the "Categories" table
    - Retrieve the API data
    - Use the API Data to populate the "Products" table


"""

# Importing the Database objects provided by the ORM and the module to that has a requester object (named 'Collector')
from food_requests import Collector
from modeles.category import Categories
from modeles.favorite import Favorites
from modeles.product import Product
from modeles.users import Users
from modules.database_service import DatabaseService

# Creation of the tables
Product.create_table()
Categories.create_table()
Favorites.create_table()
Users.create_table()

# Instantiation of a Collector
collector = Collector()

# I defined there a tuple of categories
list_of_categories = ('soup', 'pizza', 'salad', 'cake', 'cheese')

# I populate the table of the categories
for category in list_of_categories:
    category_entry = {"Name": category}
    DatabaseService.fill_categories_table(category_entry)

# I retrieve only the products that correspond to my categories in my tuple and I populate the products table
for category in list_of_categories:
    food_returned = collector.get_products_by_category(category)
    DatabaseService.fill_products_table(food_returned)
