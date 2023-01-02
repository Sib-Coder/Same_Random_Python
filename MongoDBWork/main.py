import pymongo
#подключение
db_client = pymongo.MongoClient("mongodb://localhost:27017/")#подключение к монго
db_database = db_client["sibcoder"]#подключение к БД
collection = db_database["test"]#подключение к коллекции



#добавляем 1 объект
a = {
    'name': "valrus",
    'phone': "745438577"
}
inf_add_database = collection.insert_one(a)#добавляем в бд объект из a
print(inf_add_database.inserted_id)#возвращаем id объекта

#добавляем массив объектов
a_mas = [{'name': "Ruslan", 'phone': "7447855438577"},{'name': "Vladimir", 'phone': "3844834364647"}]
inf_result = collection.insert_many(a_mas)
print(inf_result.inserted_ids)

# запрос 1 элемента
name ="Daniil"
user = collection.find_one({'name': name})
user1 = collection.count_documents({'name': name})# количество документов в коллекции у которых name
print(user, " ", user1)

# запрос всех элементов
for dan in collection.find():
    print(dan)

# Сложные запросы
#операторы смотри тут https://www.mongodb.com/docs/manual/reference/operator
name ="Daniil"
user = collection.find_one({"name":{"$eq":name}})
print(user)

# обновление документов
collection.update_one({'name': 'Daniil'}, {'$set': {'phone': 1000024}})
print(collection.find_one({'name': 'Daniil'}))
# есть ещё find_one_and_delete, find_one_and_replace и т.д.
print('Find and update')
print(collection.find_one_and_update({'name': 'Daniil'}, {'$set': {'phone': 10000}}))

#множественный update
collection.update_many({'phone': {'$gt': 100000}}, {'$set': {'phone': 210104}})
for sib in collection.find({'phone': {'$gt': 200000}}):
    print(sib)

# удаление
# delete_many, find_one_and_delete
collection.delete_one({'name': {'$regex': 'Dan'}})#юзаем регулярочку
print('После удаления:')
for sib in collection.find():
    print(sib)

# создание индексов
collection.create_index('name')  # , unique=True

# удаление коллекции
collection.drop()

# удаление бд
db_client.drop_database('sibcoder')
