import requests
import json
domain = "https://api.vk.com/method"
access_token='9bc4cbdc7d96d1dcf7f480e2436c0c118c6757c5631069800ff6fb4fae5b8300aa4de9976421e02ae630a'
v = '5.131'
fields = 'sex'

user_1=167889692
user_2=143832457
user_3=174557314
user_4=100583879

master100=[]
slave1=[]
slave2=[]
slave3=[]

def parser(user_id, warehouse):
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = requests.get(query)
    dan=(response.json()['response']['count'])
    for i in range(0,dan):
        #print(response.json()['response']['items'][i]['id'])
        warehouse.append(response.json()['response']['items'][i]['id'])
    #print(warehouse)

def results( user1, user2):
    result = list(set(user1) & set(user2))
    print(f"mutual friends ={result}")

parser(user_1,master100)
parser(user_2,slave1)
parser(user_3,slave2)
parser(user_4,slave3)
#print(f"itog=\n{master100}\n{slave1}\n{slave2}\n{slave3}")

results(master100,slave1)
results(master100,slave2)
results(master100,slave3)