"""
Project application.

This code is used to display the two initial choices.
It also allows to dive into the different interactions that follows the choice 1.
"""
# to use print the mysql data we need to  import the database management module
from modules.database_service import DatabaseService


class Interactive:
    """
    Class of command line interactions

    This class has two static methods.
    The first one is used to dive into the substitution process.
    The second one is used after choice 1 to select the category in which the user will substitute a product.
    """
    def __init__(self):
        self.first_choice()

    # I display the two options at the begining
    @staticmethod
    def first_choice():
        start_choices = ["1. Which food do you want to replace ?", "2. Display your favourite food"]
        print(f"{start_choices[0]}\n{start_choices[1]}")
        value = None
        while value not in range(1, 3):
            try:
                print("You MUST select 1 or 2!")
                value = int(input("Please enter 1 or 2:\n"))
            except ValueError:
                continue
        if value == 1:
            Interactive.choose_category()
        elif value == 2:
            print("Printing your favorites...")
            DatabaseService.show_favorites()
        else:
            print(f"You entered {value}. Bad entry. ")

    # I display the table 'Categories' in order to ask the user to select a category
    @staticmethod
    def choose_category():
        categories_table = DatabaseService.show_entire_categories_table()
        inside_options = [element for element in categories_table]
        categories_table_dict = {}
        for cat in inside_options:
            print(f"{cat['idCategories']} : {cat['Name']}\n")
            categories_table_dict.update({cat['idCategories']: cat['Name']})
        inside_choice = None
        while inside_choice not in range(1, 6):
            try:
                print("Enter a number from 1 to 5: ")
                inside_choice = int(input(f"Please enter the number of your category: "))
            except ValueError:
                continue

        # If the value entered corresponds to a category ID I have to display the OpenFoodFacts products
        # in that category
        if inside_choice in range(1, 6):
            category_selected = categories_table_dict[inside_choice]
            print(category_selected)
            DatabaseService.show_all_category_products(category_selected)
            # Now we ask the user to choose a product in the list
            # The user will substitute the chosen product
            article_to_replace_id = None
            while article_to_replace_id not in DatabaseService.articles_ids:
                try:
                    article_to_replace_id = int(input("Please enter the ID of the article the you want to replace:"))
                except ValueError:
                    continue
            if article_to_replace_id in DatabaseService.articles_ids:
                print("VALID ARTICLE")
                # If the id is valid we go to the substitution steps
                DatabaseService.show_better_products(article_to_replace_id, category_selected)
                # After the substitution we go back to the initial screen
                Interactive.first_choice()

