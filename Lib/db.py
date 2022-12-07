import mysql
import mysql.connector as mc
from configparser import ConfigParser
import Lib.read_config


# imdb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="vesselina",
#     password="Vv123456*",
#     database="imdb"
# )


class DB():
    def __init__(self):

        mysql_config = Lib.read_config.read_db_config('config.ini', 'mysql')
        # print(mysql_config)
        try:
            self.conn = mc.connect(**mysql_config)

        # self.drop_imdb_table()
        # self.create_imdb_table()
        except mc.Error as e:
            print(e)

    def create_imdb_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS imdb(
			id INT AUTO_INCREMENT PRIMARY KEY,
			title VARCHAR(100) NOT NULL,
			director VARCHAR(100) NOT NULL,
			genre VARCHAR(100) NOT NULL
			);
			"""

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def drop_imdb_table(self):
        sql = "DROP TABLE IF EXISTS imdb";

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def insert_rows(self, rows_data):
        sql = """
			INSERT IGNORE INTO title
			(title, director, genre)
			VALUES ( %s, %s, %s)
		"""

        with self.conn.cursor() as cursor:
            cursor.executemany(sql, rows_data)
            self.conn.commit()

    def insert_row(self, row_data):
        sql = """
			INSERT IGNORE INTO imdb
				(title, director, genre)
				VALUES ( %s, %s, %s)
		"""

        with self.conn.cursor(prepared=True) as cursor:
            cursor.execute(sql, tuple(row_data.values()))
            self.conn.commit()

    def select_all_data(self):
        sql = "SELECT id, title, director, genre FROM  imdb"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result

    def get_column_names(self):
        sql = "SELECT id, title, director, genre FROM imdb LIMIT 1;"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()

        return cursor.column_names

    # def delete_info_from_table(self):
    #     with self.conn.cursor() as cursor:
    #         delete from imdb


if __name__ == '__main__':
    db = DB()

    res = db.select_all_data()
    print(res)
