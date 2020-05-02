import sqlite3
import os
import datetime
from tabulate import tabulate


## create ################################################################
def create_user_tables(cursor):
    # 外部キー制約のオプションは、デフォルトでは無効になっているため、これを有効にする
    cursor.execute("PRAGMA foreign_keys = 1")

    # personsというtableを作成してみる
    # 大文字部はSQL文。小文字でも問題ない。
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR NOT NULL, 
        email VARCHAR NOT NULL, 
        password VARCHAR NOT NULL, 
        );""")

def create_task_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        task VARCHAR NOT NULL, 
        created_by INTEGER NOT NULL, 
        state VARCHAR NOT NULL, 
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        FOREIGN KEY(created_by) REFERENCES users(id)
        );""")

def register_user(cursor, name, email, password):
    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

## read ##################################################################
def todo_list(cursor):
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    result = cursor.fetchall()
    headers = list(dict(result[0]).keys())

    table = []
    for x in result:
        table.append(list(x))

    print(tabulate(table, headers, tablefmt="grid"))

## update ################################################################
# nameとpasswordで認証
def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    for x in cursor.execute(sql):
        if x['password'] != password:
            print("please check your name or password")
        else:
            print("login success!!")
            print(tuple(x))

def todo_add(cursor, user_id, task):
    sql = f"INSERT INTO tasks(task, created_by, state) VALUES('{task}', '{user_id}', 'Todo');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

def todo_doing(cursor, user, task_id):
    new_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = f"UPDATE tasks SET state='Doing' updated_at='{new_date}' WHERE id='{task_id}'"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

def todo_done(cursor, user, task_id):
    new_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = f"UPDATE tasks SET state='Done' updated_at='{new_date}' WHERE id='{task_id}'"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

def todo_remove(cursor, user, task_id):
    pass

if __name__ == '__main__':
    dir_path = 'database/'
    os.makedirs(dir_path, exist_ok=True)

    dbname = 'Task.db'
    conn = sqlite3.connect(dir_path+dbname)
    conn.row_factory = sqlite3.Row
    # sqliteを操作するカーソルオブジェクトを作成
    cursor = conn.cursor()

    create_user_tables(cursor)
    create_task_tables(cursor)
    register_user(cursor, 'AAA', 'aaa@example.com', 'aaaAAA')

    login_user(cursor, 'AAA', 'aaaAAA')

    # データベースへコミット。これで変更が反映される。
    conn.commit()
    conn.close()