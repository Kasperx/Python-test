
import mariadb
from sqlite3 import Error
import sys
import Person
from datetime import datetime

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
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    #cur.close()
    print("Created new db table 'person'.")

def create_connection():
    """ Create a database connection to sqlite database """
    conn = None
    try:
        conn = mariadb.connect(
            user="db_user",
            password="db_user_passwd",
            host="192.0.2.1",
            port=3306,
            database="person"
        )
    except Error as e:
        print(e)
    finally:
        if conn:
            #conn.close()
            return conn

def insert_data(data: [Person.Person]):
    conn = create_connection()
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
