import psycopg2
import pprint

path = "localhost"
port = "5432"
user = "postgres"
password = "postgres"

dbname = "pydb_practice"

conText = "host={} port={} dbname={} user={} password={}"
conText = conText.format(path,port,dbname,user,password)

connection = psycopg2.connect(conText)
cur = connection.cursor()

def test(cursor):
    cursor.execute("DROP TABLE IF EXISTS test")
    sql = "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
    cursor.execute(sql)

    cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cursor.execute("SELECT * FROM test;")

    for row in cursor.fetchall():
        print(row)

def test2(cur):
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

    cur.execute("SELECT * FROM users;")

    for row in cur.fetchall():
        print(row)

    cur.execute("SELECT * FROM posts;")

    for row in cur.fetchall():
        print(row)

def getAllTable(cursor):
    cursor.execute("SELECT relname as TABLE_NAME FROM pg_stat_user_tables;")
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


#test(cur)
#test2(cur)
getAllTable(cur)

# データベースへコミット。これで変更が反映される。
connection.commit()

cur.close()
connection.close()
