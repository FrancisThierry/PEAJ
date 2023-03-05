import sqlite3
from sqlite3 import Error


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_movie(conn, movie):
    """
    Create a new movie into the movies table
    :param conn:
    :param movie:
    :return: movie id
    """
    sql = ''' INSERT INTO movies(name,creation_date,director)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, movie)
    conn.commit()
    return cur.lastrowid    


if __name__ == '__main__':
    conn = create_connection(
        r"/home/thierry/Public/Travail/Projets/PEAJ/PythonLearnig/TD_Sqlite/db/pythonsqlite.db")
    sql_create = """CREATE TABLE IF NOT EXISTS movies (
	id integer PRIMARY KEY,
	name text NOT NULL,
	creation_date text,
	director text	
);"""

    # create tables
    if conn is not None:
        # create movies table
        create_table(conn, sql_create)

        # create tasks table
    else:
        print("Error! cannot create the database connection.")
    movie  = ('The Big Lebowski', '2015-01-01', "Joel and Ethan Cohen");
    create_movie(conn,movie)