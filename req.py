import requests



# url = "http://localhost:8000/authorize"
# requests.request('POST', url=url, json={"username":"Даниил",
#                                           "password":'12312s'})


url = "http://localhost:8000/get_user"
res = requests.request('GET', url=url)
print(res.json())