import sqlite3
import os
import datetime
from tabulate import tabulate

import pydb_utill
from sqlite_crud import sqlite_todo

## read ##################################################################


def todo_list(cursor):
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) > 0:
        headers = list(dict(result[0]).keys())

        table = []
        for x in result:
            table.append(list(x))

        print(tabulate(table, headers, tablefmt="grid"))


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

## delete #################################################################


def todo_remove(cursor, user, task_id):
    pass


if __name__ == '__main__':
    _, url = pydb_utill.load_db_config()

    conn = sqlite3.connect(url)
    conn.row_factory = sqlite3.Row

    # sqliteを操作するカーソルオブジェクトを作成
    cursor = conn.cursor()

    # sqlite_todo.create_user_tables(cursor)
    # sqlite_todo.create_task_tables(cursor)
    # sqlite_todo.register_user(cursor, 'AAA', 'aaa@example.com', 'aaaAAA')

    sqlite_todo.view_user_table(cursor)

#    result = sqlite_todo.isChecked(cursor, 'AAA', 'aaaAAA')
#    if result:
#        id = result['id']
#        todo_add(cursor, id, 'make todo app')
#        todo_list(cursor)

    # データベースへコミット。これで変更が反映される。
    conn.commit()
    conn.close()
