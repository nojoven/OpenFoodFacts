from modules.database_service import DatabaseService


class Interactive:

    def __init__(self):
        self.first_choice()

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
        else:
            print(value)


    @staticmethod
    def choose_category():
        better_products = []
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

        if inside_choice in range(1, 6):
            category_selected = categories_table_dict[inside_choice]
            print(category_selected)
            DatabaseService.show_all_category_products(category_selected)
            article_to_replace_id = None
            while article_to_replace_id not in DatabaseService.articles_ids:
                try:
                    article_to_replace_id = int(input("Please enter the ID of the article the you want to replace:"))
                except ValueError:
                    continue
            if article_to_replace_id in DatabaseService.articles_ids:
                print("VALID ARTICLE")
                DatabaseService.show_better_products(article_to_replace_id, category_selected)
                Interactive.first_choice()

