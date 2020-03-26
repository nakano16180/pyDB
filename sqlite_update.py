import sqlite3
import datetime
import pprint
from tabulate import tabulate

dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

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

#register_user(cursor, 'BBB', 'bbb@example.com', 'bbbBBB')
#register_user(cursor, 'CCC', 'ccc@example.com', 'cccCCC')
#register_user(cursor, 'DDD', 'ddd@example.com', 'dddDDD')

#login_user(cursor, 'AAA', 'aaa')
login_user(cursor, 'AAA', 'aaaAAA')

sql = "SELECT * FROM users"
cursor.execute(sql)
result = cursor.fetchall()
headers = list(dict(result[0]).keys())

table = []
for x in result:
    table.append(list(x))

print(tabulate(table, headers, tablefmt="grid"))


# データベースへのコネクションを閉じる。(必須)
conn.close()