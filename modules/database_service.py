import mysql.connector
from mysql.connector import errorcode


class DatabaseService:
    _instance = None
    connection = None

    @staticmethod
    def get_instance():
        if DatabaseService._instance is None:
            DatabaseService._instance = DatabaseService()
        return DatabaseService._instance

    def connect_to_mysql(self, user, password, host, database):
        try:
            self._instance.connection = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def is_connected(self):
        return self._instance is not None \
               and self._instance.connection is not None \
               and self._instance.connection.is_connected()

    def insert_category(self, names):
        cursor = self._instance.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Categories")
        res = cursor.fetchone()
        total_rows = res[0]
        print(total_rows)
        if total_rows != len(names):
            for name in names:
                add_category = ("INSERT INTO Categories "
                                "(Name) "
                                f"VALUES (%s)")

                cursor.execute(add_category, (name,))
            self._instance.connection.commit()
        cursor.close()
