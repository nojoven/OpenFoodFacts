import peewee

db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Favorites(peewee.Model):
    idProduct = peewee.PrimaryKeyField()
    productName = peewee.CharField()
    Nutrigrade = peewee.CharField()
    Stores = peewee.CharField()
    Brands = peewee.CharField()
    Category = peewee.CharField()
    Quantity = peewee.CharField()
    ReplacedID = peewee.IntegerField()
    ReplacedArticle = peewee.CharField()
    ReplacedNutrigrade = peewee.CharField()


    class Meta:
        database = db
        db_table = 'favorites'

