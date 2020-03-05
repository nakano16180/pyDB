import sqlite3
import pprint

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)

cursor = conn.cursor()
cursor.execute("select * from sqlite_master where type='table'")
for x in cursor.fetchall():
    pprint.pprint(x)
    print("-----")

# データベースへのコネクションを閉じる。(必須)
conn.close()