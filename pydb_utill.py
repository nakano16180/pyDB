import json
import pprint
from tabulate import tabulate
import datetime


def load_db_config():
    json_file = open('config.json', 'r')
    json_obj = json.load(json_file)

    username = json_obj["DB_USERNAME"]
    password = json_obj["DB_PASSWORD"]

    hostname = json_obj["DB_HOST"]
    port = json_obj["DB_PORT"]

    dbname = json_obj["DB_DATABASE"]

    db_type = json_obj["DB_CONNECTION"]

    db_url = ""
    if db_type == "postgres":
        db_url = f'postgres://{username}:{password}@{hostname}:{port}/{dbname}'
    elif db_type == "sqlite":
        db_url = f'{dbname}'

    return db_type, db_url


if __name__ == '__main__':
    db_type, url = load_db_config()
    print(db_type, url)
