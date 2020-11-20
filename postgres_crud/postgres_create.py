import datetime


def create_tables(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id serial NOT NULL PRIMARY KEY, 
        name VARCHAR NOT NULL, 
        email VARCHAR NOT NULL, 
        password VARCHAR NOT NULL, 
        remember_token VARCHAR NULL, 
        verified_at timestamp with time zone NULL, 
        created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS posts(
        id serial NOT NULL PRIMARY KEY, 
        title VARCHAR NOT NULL, 
        author_id INTEGER NOT NULL, 
        body VARCHAR NOT NULL, 
        created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        FOREIGN KEY(author_id) REFERENCES users(id)
        );""")


def register_user(cursor, name, email, password):
    sql = f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');"
    cursor.execute(sql)
    cursor.execute("COMMIT;")


def login_user(cursor, name, password):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        if x['password'] != password:
            print("please check your name or password")
        else:
            print("login success!!")
            print(tuple(x))
            new_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"UPDATE users SET verified_at='{new_date}' WHERE name='{name}'"
            cursor.execute(sql)
            cursor.execute("COMMIT;")
