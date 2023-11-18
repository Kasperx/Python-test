
import mysql.connector
import os.path
import os
import Person
from datetime import datetime

db_file: str

def create_connection():
    """ Create a database connection to sqlite database """
    conn = None
    conn = mysql.connector.connect(
        user="testuser",
        password="test",
        host="localhost",
        port="3306",
        database="testdb"
    )
    if conn:
        return conn

def create_database_and_table():
    conn = create_connection()
    sql: str = '''
        drop database if exists person;
        '''
    print("Result cmd (clean): " + sql)
    cur = conn.cursor()
    cur.execute(sql)
    sql: str = '''
    drop database if exists persontest;
    '''
    print("Result cmd (clean): " + sql)
    cur = conn.cursor()
    cur.execute(sql)
    sql: str = '''
    drop table if exists person;
    '''
    print("Result cmd (clean): " + sql)
    cur = conn.cursor()
    cur.execute(sql)
    sql: str = '''
    create database if not exists persontest;
    '''
    print("Result cmd: " + sql)
    cur = conn.cursor()
    cur.execute(sql)
    sql: str = '''
        create table person(
            id int not null auto_increment,
            name char(20),
            firstname char(20),
            email char(20),
            address char(20),
            age int,
            gender char(20),
            primary key(id)
        );
        '''
    print("Result cmd: " + sql)
    cur = conn.cursor()
    cur.execute(sql)

def insert_data(data: [Person.Person]):
    conn = create_connection()
    sql: str = '''
    insert into person(id, name, age, address)
    values
    '''
    cur = conn.cursor()

    for index, person in enumerate(data):
        sql += ("("
        + str(person.id) + ", "
        + "'" + person.name + "'" + ", "
        + str(person.age) + ", "
        + "'" + person.address + "'" + ", "
        #+ "'" + datetime.today().strftime('%Y-%m-%d') + "'"
        + ")")
        if index < (len(data) -1 ):
            sql += ", "
    print("Result cmd: " + sql)

    cur.execute(sql)
    conn.commit()
    return cur.lastrowid
