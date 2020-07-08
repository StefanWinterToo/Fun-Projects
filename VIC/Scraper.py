import pandas as pd
import re


file = open("vic.txt", "r")
data = file.read()
file.close()
data = data.split("\n")

def extract_user(l):
    user_position = []
    for i in range(len(l)):
        if "BY" in l[i]:
            user_position.append(i)
    return([l[i] for i in user_position])

user_list = extract_user(data)
print(user_list)
