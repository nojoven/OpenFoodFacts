"""

Obtaining python objects to manage the database.

The ORM is Peewee.
Here I define the columns and the data types of the entries for the table Users.

"""
import peewee

# Connection to the Mysql database 'purbeurre'
db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Users(peewee.Model):
    """

    Users table content

   There are three columns:
   - one for the user ID
   - one for the username
   - one for his password
    """
    UserID = peewee.PrimaryKeyField()
    Username = peewee.CharField()
    password = peewee.CharField()

    # A getter is necessary to process the data using python
    @staticmethod
    def get_db():
        return db

    # Metadata used by the ORM
    class Meta:
        database = db
        db_table = 'users'
