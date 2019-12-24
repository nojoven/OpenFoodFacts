import peewee

db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Favorites(peewee.Model):
    idProduct = peewee.IntegerField()
    productName = peewee.CharField()

    class Meta:
        database = db
        db_table = 'favorites'

