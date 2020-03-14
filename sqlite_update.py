import sqlite3
import pprint

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def register_user(cursor, name, email, password):
    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")

def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    for x in cursor.execute(sql):
        print(x['password'] == password)

#register_user(cursor, 'BBB', 'bbb@example.com', 'bbbBBB')
#register_user(cursor, 'CCC', 'ccc@example.com', 'cccCCC')
#register_user(cursor, 'DDD', 'ddd@example.com', 'dddDDD')

sql = "select * from users"
cursor.execute(sql)
for x in cursor.fetchall():
    pprint.pprint(tuple(x))
    print("-----")

login_user(cursor, 'AAA', 'aaa')
login_user(cursor, 'AAA', 'aaaAAA')

# データベースへのコネクションを閉じる。(必須)
conn.close()