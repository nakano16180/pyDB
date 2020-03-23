import psycopg2
import pprint
from tabulate import tabulate
import datetime
from psycopg2.extras import DictCursor

username = "postgres"
password = "postgres"

hostname = "localhost"
port = "5432"

dbname = "pydb_practice"

db_url = f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}'
connection = psycopg2.connect(db_url)
cur = connection.cursor(cursor_factory=DictCursor)

def create_view(cur):
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    headers = [col.name for col in cur.description]

    table = []
    for x in result:
        table.append(list(x))

    print(tabulate(table, headers, tablefmt="grid"))

def create_tables(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id serial NOT NULL PRIMARY KEY, 
        name VARCHAR NOT NULL, 
        email VARCHAR NOT NULL, 
        password VARCHAR NOT NULL, 
        remember_token VARCHAR NULL, 
        verified_at timestamp with time zone NULL, 
        created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS posts(
        id serial NOT NULL PRIMARY KEY, 
        title VARCHAR NOT NULL, 
        author_id INTEGER NOT NULL, 
        body VARCHAR NOT NULL, 
        created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        FOREIGN KEY(author_id) REFERENCES users(id)
        );""")

## read
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

## update
def register_user(cursor, name, email, password):
    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

# nameとpasswordで認証
def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        if x['password'] != password:
            print("please check your name or password")
        else:
            print("login success!!")
            print(tuple(x))
            new_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"UPDATE users SET verified_at='{new_date}' WHERE name='{name}'"
            cursor.execute(sql)
            cursor.execute("COMMIT;")

## delete
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

#create_tables(cur)

#getAllTable(cur)
#getAllCollumByTableName(cur, 'users')
#getAllCollumByTableName(cur, 'posts')

#register_user(cur, 'AAA', 'aaa@example.com', 'aaaAAA')
#register_user(cur, 'BBB', 'bbb@example.com', 'bbbBBB')
#register_user(cur, 'CCC', 'ccc@example.com', 'cccCCC')
#register_user(cur, 'DDD', 'ddd@example.com', 'dddDDD')

#login_user(cur, 'AAA', 'aaaAAA')

#deleteUserByName(cur, 'DDD', 'dddDDD')

create_view(cur)

# データベースへコミット。これで変更が反映される。
connection.commit()

cur.close()
connection.close()
