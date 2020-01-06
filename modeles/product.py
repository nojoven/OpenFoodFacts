"""

Obtaining python objects to manage the database.

The ORM is Peewee.
Here I define the columns and the data types of the entries for the table Products.

"""
import peewee

# Connection to the Mysql database 'purbeurre'
db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Product(peewee.Model):
    """

    Products table content

   There are seven columns:
   - one for the ID which is the primary key
   - one for the name of the product
   - one for the stores where you can buy it
   - one for the brands that use to sell the product
   - one for the name of its category
   - one for its quantity (volume, mass, etc)

    """
    idProduct = peewee.PrimaryKeyField()
    ProductName = peewee.CharField()
    Stores = peewee.CharField()
    Brands = peewee.CharField()
    Nutrigrade = peewee.CharField()
    Category = peewee.CharField()
    Quantity = peewee.CharField()

    # A getter is necessary to process the data using python
    @staticmethod
    def get_db():
        return db

    # Metadata used by the ORM
    class Meta:
        database = db
        db_table = 'products'
