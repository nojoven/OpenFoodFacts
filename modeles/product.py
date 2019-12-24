import peewee

db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Product(peewee.Model):
    idProduct = peewee.PrimaryKeyField()
    ProductName = peewee.CharField()
    Stores = peewee.CharField()
    Brands = peewee.CharField()
    Nutrigrade = peewee.CharField()
    Category = peewee.CharField()
    Quantity = peewee.CharField()

    @staticmethod
    def get_db():
        return db

    class Meta:
        database = db
        db_table = 'products'
