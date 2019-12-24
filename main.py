from food_requests import Collector
from modules.database_service import DatabaseService
import terminal_app as tapp

collector = Collector()
list_of_categories = ('soup', 'pizza', 'salad', 'cake', 'cheese')


#for category in list_of_categories:
 #   food_returned = collector.get_products_by_category(category)
 #   DatabaseService.fill_products_table(food_returned)
category_selected = None
term = tapp.Interactive()



# for category in list_of_categories:
  #   category_entry = {"Name": category}
  #   db.fill_categories_table(category_entry)



