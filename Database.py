
import sqlite3
from sqlite3 import Error
import os.path
import os
import Person
from datetime import datetime

db_file: str

def create_file_if_not_exists(file_path = None):
    if file_path is None:
        file_path = os.path.abspath(os.getcwd()) + "/database.sqlite3"
        db_file = file_path
    if not os.path.exists(db_file):
        file = open(db_file, 'w')
        file.close()
    return db_file

def create_database():
    sql: str = (""
    + "create table if not exists "
    + "Person( "
    #+ "id integer primary key autoincrement, "
    + "id integer, "
    + "name varchar, "
    + "age integer, "
    + "address varchar, "
    + "date varchar"
    ")")
    db_file = create_file_if_not_exists()
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    #cur.close()
    print("Created new db table 'person'.")

def create_connection(db_file):
    """ Create a database connection to sqlite database """
    conn = None
    db_file = create_file_if_not_exists()
    try:
        conn = sqlite3.connect(db_file)
        print("Created db file with sqlite with version: " + sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            #conn.close()
            return conn

def insert_data(data: [Person.Person]):
    conn = create_connection(None)
    db_file = create_file_if_not_exists()
    sql: str = '''
    insert into Person(id, name, age, address, date)
    values
    '''
    cur = conn.cursor()

    for index, person in enumerate(data):
        sql += ("("
        + str(person.id) + ", "
        + "'" + person.name + "'" + ", "
        + str(person.age) + ", "
        + "'" + person.address + "'" + ", "
        + "'" + datetime.today().strftime('%Y-%m-%d') + "'"
        #+ "datetime('now','localdate')"
        + ")")
        if index < (len(data) -1 ):
            sql += ", "
    print("Result cmd: " + sql)

    cur.execute(sql)
    conn.commit()
    return cur.lastrowid
