import sqlite3
import pprint

dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)

cursor = conn.cursor()

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

getAllCollumByTableName(cursor, 'users')
getAllCollumByTableName(cursor, 'posts')

# データベースへのコネクションを閉じる。(必須)
conn.close()