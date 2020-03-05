## Python Database

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
$ pythton3 python_db.py
```


### Sqlite

To create database
```
$ python3 sqlite_create.py
```

To read data
```
$ python3 sqlite_read.py
```