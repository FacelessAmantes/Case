# import mysql.connector
# from mysql.connector import Error

# def create_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             password=user_password,
#             database=db_name
#         )
#         print("Подключение к MySQL успешно")
#     except Error as e:
#         print(f"Ошибка '{e}' при подключении к MySQL")
    
#     return connection

# # Замените параметры на свои
# host = "194.87.92.35"  # или IP-адрес вашего сервера
# user = "bot"
# password = "HcKFNGtJesicDrYe"
# database = "test"

# connection = create_connection(host, user, password, database)

# # Не забудьте закрыть соединение после использования
# if connection:
#     connection.close()

import json

with open('result.json','r', encoding='UTF-8') as fp:
    data = json.load(fp=fp)

import requests


# for d in data.items():
#     print(d)
url = 'http://localhost:8001/get_articals?limit=1000'

response = requests.request('GET', url=url)

print(response.content)