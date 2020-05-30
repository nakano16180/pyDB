## Python Database

### Python setup

```
$ git clone https://github.com/nakano16180/pyDB.git
$ cd pyDB/
$ pipenv install
```

### Postgresql
#### setup
create database

```
$ docker run -v /var/lib/psql --name psql_data busybox
$ docker run --volumes-from psql_data --name psql -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:9.6
```

```
$ docker exec -it psql bash
# psql -h localhost -U postgres

postgres=# create database pydb_practice;
postgres=# \q

# exit
```

#### run

```
$ pipenv run pythton python_db.py
```


### Sqlite

```
$ mkdir database/
$ pipenv run python sqlite_app.py
```

### 参考資料
- https://crimnut.hateblo.jp/entry/2018/04/17/172709
- http://memopy.hatenadiary.jp/entry/2017/03/05/231859
- https://nekodeki.com/python%E3%81%A7sqlite3%E3%82%92%E4%BD%BF%E3%81%86/
- https://note.nkmk.me/python-f-strings/
- https://docs.python.org/ja/3/library/sqlite3.html#sqlite3.Row