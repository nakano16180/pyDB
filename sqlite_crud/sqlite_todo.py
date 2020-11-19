from tabulate import tabulate


def create_user_tables(cursor):
    # 外部キー制約のオプションは、デフォルトでは無効になっているため、これを有効にする
    cursor.execute("PRAGMA foreign_keys = 1")

    # personsというtableを作成してみる
    # 大文字部はSQL文。小文字でも問題ない。
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR NOT NULL, 
        email VARCHAR NOT NULL, 
        password VARCHAR NOT NULL
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
    sql = f"SELECT * FROM users WHERE name='{name}'"
    for x in cursor.execute(sql):
        if x['email'] == email:
            print("already exists")
            return

    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")


def view_user_table(cursor):
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) > 0:
        headers = list(dict(result[0]).keys())

        table = []
        for x in result:
            table.append(list(x))

        print(tabulate(table, headers, tablefmt="grid"))


def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    for x in cursor.execute(sql):
        if x['password'] == password:
            return x


def isChecked(cursor, name, password):
    result = login_user(cursor, name, password)
    if result:
        return result
    else:
        print("please check your name or password")


def delete_user(cursor, name, password):
    sql = f"DELETE FROM users WHERE name='{name}'"
    cursor.execute(sql)
    cursor.execute("COMMIT;")
