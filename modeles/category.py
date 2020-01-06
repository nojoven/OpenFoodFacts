"""

Obtaining python objects to manage the database.

The ORM is Peewee.
Here I define the columns and the data types of the entries for the table Category.

"""
import peewee

# Connection to the Mysql database 'purbeurre'
db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Categories(peewee.Model):
    """

    Categories table content

   There are two columns:
   - one for the ID which is the primary key
   - and one for the name of the category

    """
    idCategories = peewee.PrimaryKeyField()
    Name = peewee.CharField()

    # A getter is necessary to process the data using python
    @staticmethod
    def get_db():
        return db

    # Metadata used by the ORM
    class Meta:

        database = db
        db_table = 'categories'
