import requests

BASE = "http://127.0.0.1:5000/"

""" response = requests.put(BASE + "person/Fredi", {"id": 3, "username": "frd", "age": 1})
print(response.json())
input()
response = requests.get(BASE + "person/Fredi")
print(response.json()) """
response = requests.get(BASE + "person/Fredi")
print(response.json())