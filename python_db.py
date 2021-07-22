import psycopg2
import pprint
from tabulate import tabulate
import datetime
from psycopg2.extras import DictCursor

import pydb_utill
from postgres_crud import postgres_create

hostname = "localhost"
port = "5432"

dbname = "pydb_practice"

db_url = f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}'#default connection destination
connection = psycopg2.connect(db_url)
cur = connection.cursor(cursor_factory=DictCursor)


def commit_change(connection):connection.commit()
def change_connection_destination(sync=True):]
    global cur,connection,db_url
    if sync:commit_change()
    cur.close()
    connection.close()
    connection = psycopg2.connect(f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}')
    cur = connection.cursor(cursor_factory=DictCursor)
def reconnect(sync=True):
    change_connection_destination(sync,db_url)
def set_connection_details(key,value):
    global username,password,hostname,port,dbname
    if key=="username":username=value
    elif key=="password":password=value
    elif key=="hostname":hostname=value
    elif key=="port":port=value
    elif key=="dbname":dbname=value
def create_view(cur):
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    headers = [col.name for col in cur.description]

    table = []
    for x in result:
        table.append(list(x))

    print(tabulate(table, headers, tablefmt="grid"))


def getAllTable(cursor):
    cursor.execute("SELECT relname as TABLE_NAME FROM pg_stat_user_tables;")
    for x in cursor.fetchall():
        pprint.pprint(x)
        print("-----")


def getAllCollumByTableName(cursor, table_name):
    sql = f"SELECT * FROM {table_name};"
    cursor.execute(sql)
    colnames = [col.name for col in cursor.description]
    print(colnames)
    print("------------------")

# delete


def deleteUserByName(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        if x['password'] != password:
            print("please check your name or password")
        else:
            sql = f"DELETE FROM users WHERE name='{name}';"
            cursor.execute(sql)
            cursor.execute("COMMIT;")


if __name__ == '__main__':
    db_type, url = pydb_utill.load_db_config()

    if not db_type == 'postgresql':
        return

    connection = psycopg2.connect(url)
    cur = connection.cursor(cursor_factory=DictCursor)

    # postgres_create.create_tables(cur)

    # getAllTable(cur)
    #getAllCollumByTableName(cur, 'users')
    #getAllCollumByTableName(cur, 'posts')

    #postgres_create.register_user(cur, 'AAA', 'aaa@example.com', 'aaaAAA')
    #postgres_create.register_user(cur, 'BBB', 'bbb@example.com', 'bbbBBB')
    #postgres_create.register_user(cur, 'CCC', 'ccc@example.com', 'cccCCC')
    #postgres_create.register_user(cur, 'DDD', 'ddd@example.com', 'dddDDD')

    #postgres_create.login_user(cur, 'AAA', 'aaaAAA')

    #deleteUserByName(cur, 'DDD', 'dddDDD')

    create_view(cur)

    # データベースへコミット。これで変更が反映される。
    connection.commit()

    cur.close()
    connection.close()
