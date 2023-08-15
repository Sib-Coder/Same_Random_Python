import json
import sqlite3
import time

import redis


def createdb():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    #cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
    cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
    cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
    connection.commit()
    connection.close()
    print(rows)

def get_user_fish():
    #открывашки
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    redis_client = redis.Redis(password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81")

    cache_value = redis_client.get("user_fish") #работа с кешем
    if cache_value is not None:
        print("cache:")
        return json.loads(cache_value)

    res = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall() #если нет значения то добавим в кеш
    data =json.dumps(res)
    redis_client.set("user_fish",data, ex=100 ) # ex= таймер удаления

    #закрывашки
    cursor.close()
    redis_client.close()
    return res


if __name__ == '__main__':
    print(get_user_fish())


