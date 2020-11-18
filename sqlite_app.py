import sqlite3
import pprint
import datetime
from tabulate import tabulate

import pydb_utill
from sqlite_crud import sqlite_create
from sqlite_crud import sqlite_read
from sqlite_crud import sqlite_update


def create_view(cur):
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    headers = list(dict(result[0]).keys())

    table = []
    for x in result:
        table.append(list(x))

    print(tabulate(table, headers, tablefmt="grid"))


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
    _, url = pydb_utill.load_db_config()

    conn = sqlite3.connect(url)
    conn.row_factory = sqlite3.Row

    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    # sqlite_create.create_tables(cur)
    # sqlite_read.getAllTable(cur)
    print('--display users table')
    sqlite_read.getAllCollumByTableName(cur, 'users')
    print('--display posts table')
    sqlite_read.getAllCollumByTableName(cur, 'posts')

    #sqlite_update.register_user(cur, 'AAA', 'aaa@example.com', 'aaaAAA')
    #sqlite_update.register_user(cur, 'BBB', 'bbb@example.com', 'bbbBBB')
    #sqlite_update.register_user(cur, 'CCC', 'ccc@example.com', 'cccCCC')
    #sqlite_update.register_user(cur, 'DDD', 'ddd@example.com', 'dddDDD')

    print('--display users table')
    sqlite_update.view_user_table(cur)
    sqlite_update.login_user(cur, 'AAA', 'aaaAAA')

    # データベースへコミット。これで変更が反映される。
    conn.commit()
    conn.close()
