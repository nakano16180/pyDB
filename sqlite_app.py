import sqlite3
import pprint
import datetime
from tabulate import tabulate

dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)
conn.row_factory = sqlite3.Row
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

def create_view(cur):
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    headers = list(dict(result[0]).keys())

    table = []
    for x in result:
        table.append(list(x))

    print(tabulate(table, headers, tablefmt="grid"))


def create_tables(cursor):
    # 外部キー制約のオプションは、デフォルトでは無効になっているため、これを有効にする
    cursor.execute("PRAGMA foreign_keys = 1")

    # personsというtableを作成してみる
    # 大文字部はSQL文。小文字でも問題ない。
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR NOT NULL, 
        email VARCHAR NOT NULL, 
        password VARCHAR NOT NULL, 
        remember_token VARCHAR NULL, 
        verified_at DATETIME NULL, 
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS posts(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        title VARCHAR NOT NULL, 
        author_id INTEGER NOT NULL, 
        body VARCHAR NOT NULL, 
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        FOREIGN KEY(author_id) REFERENCES users(id)
        );""")

def getAllTable(cursor):
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    for x in cursor.fetchall():
        pprint.pprint(tuple(x))
        print("-----")

def getAllCollumByTableName(cursor, table_name):
    print("------------------")
    sql = f"SELECT * FROM {table_name};"
    cursor.execute(sql)
    for x in cursor.fetchall():
        pprint.pprint(tuple(x))
        print("-----")

def register_user(cursor, name, email, password):
    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

# nameとpasswordで認証
def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    for x in cursor.execute(sql):
        if x['password'] != password:
            print("please check your name or password")
        else:
            print("login success!!")
            print(tuple(x))
            new_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"UPDATE users SET verified_at='{new_date}' WHERE name='{name}'"
            cursor.execute(sql)
            cursor.execute("COMMIT;")

def deleteUserByName(cursor, name):
    sql = "DELETE FROM users WHERE name='{name}';"
    cursor.execute(sql)
    cursor.execute("COMMIT;")


getAllCollumByTableName(cur, 'users')
getAllCollumByTableName(cur, 'posts')

#register_user(cursor, 'BBB', 'bbb@example.com', 'bbbBBB')
#register_user(cursor, 'CCC', 'ccc@example.com', 'cccCCC')
#register_user(cursor, 'DDD', 'ddd@example.com', 'dddDDD')

login_user(cur, 'AAA', 'aaaAAA')


# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()