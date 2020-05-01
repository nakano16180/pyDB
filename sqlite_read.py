import sqlite3
import pprint
import os

def getAllTable(cursor):
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    for x in cursor.fetchall():
        pprint.pprint(x)
        print("-----")

def getAllCollumByTableName(cursor, table_name):
    print("------------------")
    sql = f"SELECT * FROM {table_name};"
    cursor.execute(sql)
    for x in cursor.fetchall():
        pprint.pprint(x)
        print("-----")

if __name__ == '__main__':
    dir_path = 'database/'
    os.makedirs(dir_path, exist_ok=True)

    dbname = 'TEST.db'
    conn = sqlite3.connect(dir_path+dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cursor = conn.cursor()
    
    getAllTable(cursor)
    getAllCollumByTableName(cursor, 'users')
    getAllCollumByTableName(cursor, 'posts')


    # データベースへコミット。これで変更が反映される。
    conn.commit()
    # データベースへのコネクションを閉じる。(必須)
    conn.close()