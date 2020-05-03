import sqlite3
import datetime
import os
import pprint
from tabulate import tabulate

def view_user_table(cursor):
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) > 0:
        headers = list(dict(result[0]).keys())

        table = []
        for x in result:
            table.append(list(x))

        print(tabulate(table, headers, tablefmt="grid"))

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

if __name__ == '__main__':
    dir_path = 'database/'
    os.makedirs(dir_path, exist_ok=True)

    dbname = 'TEST.db'
    conn = sqlite3.connect(dir_path+dbname)
    conn.row_factory = sqlite3.Row
    # sqliteを操作するカーソルオブジェクトを作成
    cursor = conn.cursor()
    
    #register_user(cursor, 'AAA', 'aaa@example.com', 'aaaAAA')
    #register_user(cursor, 'BBB', 'bbb@example.com', 'bbbBBB')
    #register_user(cursor, 'CCC', 'ccc@example.com', 'cccCCC')
    #register_user(cursor, 'DDD', 'ddd@example.com', 'dddDDD')

    #login_user(cursor, 'AAA', 'aaa')
    login_user(cursor, 'AAA', 'aaaAAA')
    
    view_user_table(cursor)

    # データベースへのコネクションを閉じる。(必須)
    conn.close()