import sqlite3
import pprint

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)

cursor = conn.cursor()

def deleteUserByName(cursor, name):
    sql = "DELETE FROM users WHERE name='{name}';"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

sql = "select * from users"
cursor.execute(sql)
for x in cursor.fetchall():
    pprint.pprint(x)
    print("-----")

# データベースへのコネクションを閉じる。(必須)
conn.close()