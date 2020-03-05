import psycopg2

path = "localhost"
port = "5432"
user = "postgres"
password = "postgres"

dbname = "pydb_practice"

conText = "host={} port={} dbname={} user={} password={}"
conText = conText.format(path,port,dbname,user,password)


connection = psycopg2.connect(conText)
cur = connection.cursor()

sql = "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
cur.execute(sql)

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cur.execute("SELECT * FROM test;")

for row in cur:
    print(row)

cur.close()
connection.close()
