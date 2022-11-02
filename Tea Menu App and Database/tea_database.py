import sqlite3

Create_Tea_Table = "CREATE TABLE IF NOT EXISTS teas (id INTEGER PRIMARY KEY, type TEXT, country TEXT, rating INTEGER);"
Insert_Tea = "INSERT INTO teas (type, country, rating) VALUES (?, ?, ?);"

Get_All_Teas = "SELECT * FROM teas;"
Get_Teas_By_Type = "SELECT * FROM teas WHERE type = ?;"
Get_Country_Origin = """
SELECT * FROM teas
WHERE type = ?
ORDER BY rating DESC
LIMIT 1;"""

def connect():
    return sqlite3.connect("tea_data.db")

connection = connect()

def create_tables(connection):
    with connection:
        connection.execute(Create_Tea_Table)

def insert_tea(connection, type, country, rating):
    with connection:
        connection.execute(Insert_Tea, (type, country, rating))

def get_all_teas(connection):
    with connection:
        return connection.execute(Get_All_Teas).fetchall()

def get_teas_by_type(connection, type):
    with connection:
        return connection.execute(Get_Teas_By_Type, (type,)).fetchall()

def country_origin(connection, type):
    with connection:
        return connection.execute(Get_Country_Origin, (type,)).fetchone()