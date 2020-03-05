import sqlite3

dir_path = 'database/'
dbname = 'TEST.db'
conn = sqlite3.connect(dir_path+dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# 外部キー制約のオプションは、デフォルトでは無効になっているため、これを有効にする
cur.execute("PRAGMA foreign_keys = 1")


# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    password VARCHAR NOT NULL, 
    remember_token VARCHAR NULL, 
    verified_at DATETIME NULL, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS posts(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR NOT NULL, 
    author_id INTEGER NOT NULL, 
    body VARCHAR NOT NULL, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
    FOREIGN KEY(author_id) REFERENCES users(id)
    )""")

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()