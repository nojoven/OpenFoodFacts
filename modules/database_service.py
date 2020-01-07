"""
Data management code

This file is used to interact with the database in order to display and manipulate the data
depending on the user actions in the terminal.
It uses the orm objects Product, Categories and Favorites

"""
from modeles.product import Product
from modeles.category import Categories
from modeles.favorite import Favorites


class DatabaseService:
    """
    DatabaseServices

    Class created to provide statics methods that allows my terminal app do deal with the mysql data.
    Being static makes the call of DatabaseService's functions easier.
    """

    # I created this list here to be accessible inside the methods
    articles_ids = []

    # Insert multiple data at a time in multiple rows in (table Product)
    @staticmethod
    def fill_products_table(plist):
        with Product.get_db().atomic():
            query = Product.insert_many(plist)
            query.execute()

    # Insert multiple data at a time in multiple rows in (table Categories)
    @staticmethod
    def fill_categories_table(category):
        with Categories.get_db().atomic():
            query = Categories.insert_many(category)
            query.execute()

    # Returns the content of the table Categories
    @staticmethod
    def show_entire_categories_table():
        categories_table = Categories.select().dicts()
        return categories_table

    # Prints the products that correspond to the category selected by the user
    @staticmethod
    def show_all_category_products(category_selected):
        entire_category = Product.select().where(Product.Category == category_selected).dicts()
        for article in entire_category:
            DatabaseService.articles_ids.append(article['idProduct'])
            print(f"{article['idProduct']} : {article['ProductName']}")

    # Prints in the category selected
    # the products that have a better nutrigrade than the substituted product
    @staticmethod
    def show_better_products(product_id, category_selected):
        """
        Substitution process

        This method starts with the display of the better products.
        Then the user is asked to select a preferred product.
        Finally the preferred product is saved in the table 'Favorite'.
        """
        product_data = Product.select().where(Product.idProduct == product_id).get()
        product_nutrigrade = product_data.Nutrigrade
        print(f"Nutrigrade is {product_nutrigrade}. ")
        better_products = Product.select().where((Product.Category == category_selected) &
                                                 (Product.Nutrigrade < product_nutrigrade))

        if len(better_products) != 0:
            better_ids = []
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
                good_id = better_choice
                good_category = good_product.Category
                good_brands = good_product.Brands
                good_stores = good_product.Stores
                good_quantity = good_product.Quantity
                print(f"You don't like \n{product_data.idProduct}--{product_data.ProductName} "
                      f"\n--Nutrigrade = {product_data.Nutrigrade}. \n"
                      f"You prefer {better_choice}---{good_product.ProductName}. \n"
                      f"Nutrigrade = {good_product.Nutrigrade} "
                      f" \n Favorites table edition...")
                DatabaseService.save_preference(good_id, good_category, good_product.ProductName,
                                                good_product.Nutrigrade, good_stores, good_brands, good_quantity,
                                                product_data.idProduct, product_data.ProductName,
                                                product_data.Nutrigrade)
        else:
            print("The nutriscore is already 'A'. There is no better product.")

    # Saves the preferred product with some data about the replaced one in the table 'Favorites'
    @staticmethod
    def save_preference(preferred_id, preferred_category, preferred_name, preferred_grade,
                        preferred_stores, preferred_brands, preferred_quantity,
                        replaced_id, replaced_name, replaced_grade):
        query = Favorites.insert(ProductID=preferred_id, Name=preferred_name, Nutrigrade=preferred_grade,
                                 Category=preferred_category, Stores=preferred_stores,
                                 Brands=preferred_brands, Quantity=preferred_quantity,
                                 ReplacedID=replaced_id, ReplacedArticle=replaced_name,
                                 ReplacedNutrigrade=replaced_grade)
        query.execute()
        print("Favorites updated. ")

    # Displays the content of the table Favorites
    @staticmethod
    def show_favorites():
        favorites_table = Favorites.select().dicts()
        for fav in favorites_table:
            print(f"{fav} \n")
