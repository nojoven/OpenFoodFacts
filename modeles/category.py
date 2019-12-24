import peewee

db = peewee.MySQLDatabase('purbeurre', user='root', password='Hamzamal89', host='127.0.0.1', port=3306)


class Categories(peewee.Model):
    idCategories = peewee.PrimaryKeyField()
    Name = peewee.CharField()

    @staticmethod
    def get_db():
        return db

    class Meta:

        database = db
        db_table = 'categories'
