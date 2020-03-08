import sqlite3
import pprint

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)

cursor = conn.cursor()
cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
for x in cursor.fetchall():
    pprint.pprint(x)
    print("-----")

print("------------------")
sql = "SELECT * FROM users;"
cursor.execute(sql)
for x in cursor.fetchall():
    pprint.pprint(x)
    print("-----")

print("------------------")
sql = "SELECT * FROM posts;"
cursor.execute(sql)
for x in cursor.fetchall():
    pprint.pprint(x)
    print("-----")

# データベースへのコネクションを閉じる。(必須)
conn.close()