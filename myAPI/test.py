import requests
from database import PersonModel

BASE = "http://127.0.0.1:5000/"

""" response = requests.put(BASE + "person/Fredi", {"id": 3, "username": "frd", "age": 1})
print(response.json())
input()
response = requests.get(BASE + "person/Fredi")
print(response.json()) """

# response = requests.get(BASE + "person/Fredi")
# print(response.json())

"""
data = [{'username': "Stefan", 'age': 25}]

for i in range(len(data)):
    response = requests.put(BASE + "person/" + str[i], data[i])
    print(response.json())

input()
response = requests.get(BASE + "person/0")
print(response.json())
"""

# Query Database
records = PersonModel.query.all()

if records:
    for record in records:
        print(record.username, ": ", record.age)
        #print(record.__dict__['username'])
        #print(f"<id={record.id}, username={record.username}, age = {record.age}>")
        #print("")
else:
    print("No data in database")