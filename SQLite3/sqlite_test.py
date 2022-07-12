'''
    sqlite3 seems to be included in python 3.5 or earlier but just in case...
    pip3 install pysqlite3
    and
    sudo apt-get install sqlitebrowser
'''

import sqlite3
from sqlite3 import Error

""" 
    create a database connection to a SQLite database if exists
    OR
    create a new SQLite database file otherwise
"""
def create_connection(db_file):
    '''
        pass a filename or ':memory:' to have a db in ram
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def execute_query(query, connection):
    try:
        return  connection.execute(query)
    except Error as e:
        print(e)
    return None


def insert_data(data, connection):
    sql = 'insert into rank values (?, ?)'
    cursor = connection.execute(sql, data)
    return cursor

#----------------------------------------------------------------------

# create connection (or create database)
con = create_connection("test.sqlite")

#create a table
create_sql = """
                CREATE TABLE IF NOT EXISTS rank (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                );
            """
cursor = execute_query(create_sql, con)


# insert data using placeholders
cursor = insert_data ( (1, 'John') , con)


# send changes to db permanently
con.commit()


# get data 
cursor = execute_query("select * from rank", con)
data = cursor.fetchall()


"""

Other useful commands


cursor.fetchone()
cursor.fetchmany([size = cursor.arraysize])
cursor.fetchall()

connection.close()

"""

