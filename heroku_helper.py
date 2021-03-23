import psycopg2
import pprint
from tabulate import tabulate
import datetime

from psycopg2.extras import DictCursor

import pydb_utill


def getAllTable(cursor):
    cursor.execute("SELECT relname as TABLE_NAME FROM pg_stat_user_tables;")
    for x in cursor.fetchall():
        pprint.pprint(x)
        print("-----")

def insert(cursor, sqlStr):
    cursor.execute('BEGIN')
    cursor.execute(sqlStr)
    cursor.execute('COMMIT')

if __name__ == '__main__':
    db_type, url = pydb_utill.load_db_config()

    if db_type == 'postgres':

        connection = psycopg2.connect(url)
        cur = connection.cursor(cursor_factory=DictCursor)

        getAllTable(cur)

        sql = 'ALTER TABLE posts ALTER COLUMN body TYPE text'
        insert(cur, sql)

        cur.close()
        connection.close()
