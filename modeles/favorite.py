"""

Obtaining python objects to manage the database.

The ORM is Peewee.
Here I define the columns and the data types of the entries for the table Favorites.

"""
import peewee

# Connection to the Mysql database 'purbeurre'
db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Favorites(peewee.Model):
    """

    Favorites table content

   There are twelve columns:
   - one for the favorite ID which is the primary key
   - one for the ID of the favorite product in the table Products
   - one for the name of the favorite
   - One for the nutrigrade of the favorite
   - one for the stores where you can buy the favorite
   - one for the brands that use to sell the favorite
   - one for the name of the favorite's category
   - one for the favorite's quantity (volume, mass, etc)
   - one for the ID of the article substituded by the favorite
   - one for the name of the article that has been replaced by the favorite
   - one for the nutrigrade of the article that has been replaced by the favorite
   - one for the user who adds the favorite
    """
    FavoriteID = peewee.PrimaryKeyField()
    ProductID = peewee.IntegerField()
    Name = peewee.CharField()
    Nutrigrade = peewee.CharField()
    Stores = peewee.CharField()
    Brands = peewee.CharField()
    Category = peewee.CharField()
    Quantity = peewee.CharField()
    ReplacedID = peewee.IntegerField()
    ReplacedArticle = peewee.CharField()
    ReplacedNutrigrade = peewee.CharField()
    UserID = peewee.CharField()

    # A getter is necessary to process the data using python
    @staticmethod
    def get_db():
        return db

    # Metadata used by the ORM
    class Meta:
        database = db
        db_table = 'favorites'

