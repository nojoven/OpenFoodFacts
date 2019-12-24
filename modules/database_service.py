import peewee as p
import _json
from modeles.product import Product
from modeles.category import Categories


class DatabaseService:
    articles_ids = []

    @staticmethod
    def fill_products_table(plist):
        with Product.get_db().atomic():
            query = Product.insert_many(plist)
            query.execute()

    @staticmethod
    def fill_categories_table(category):
        with Categories.get_db().atomic():
            query = Categories.insert_many(category)
            query.execute()

    @staticmethod
    def show_entire_categories_table():
        categories_table = Categories.select().dicts()
        return categories_table

    @staticmethod
    def show_all_category_products(category_selected):
        entire_category = Product.select().where(Product.Category == category_selected).dicts()
        for article in entire_category:
            DatabaseService.articles_ids.append(article['idProduct'])
            print(f"{article['idProduct']} : {article['ProductName']}")

    @staticmethod
    def show_better_products(product_id, category_selected):
        product_data = Product.select().where(Product.idProduct == product_id).get()
        product_nutrigrade = product_data.Nutrigrade
        print(f"Nutrigrade is {product_nutrigrade}. ")
        better_products = Product.select().where((Product.Category == category_selected) &
                                                 (Product.Nutrigrade < product_nutrigrade))
        better_ids = []
        good_product = None
        for better in better_products:
            print(f"{better.idProduct}---{better.ProductName}:{better.Nutrigrade}")
            better_ids.append(better.idProduct)

        better_choice = None
        while better_choice not in better_ids:
            try:
                print("Choose a product to replace the bad product.")
                better_choice = int(input("Enter the ID of a better product: "))
            except ValueError:
                continue
        if better_choice in better_ids:
            good_product = Product.select().where(Product.idProduct == better_choice).get()
            print(f"You don't like{product_data.idProduct}--{product_data.ProductName} "
                  f"\n--Nutrigrade = {product_data.Nutrigrade} "
                  f"You prefer {good_product.idProduct}---{good_product.ProductName}. "
                  f"Nutrigrade = {good_product.Nutrigrade} "
                  f"\nFavorites table edited.")


    @staticmethod
    def update