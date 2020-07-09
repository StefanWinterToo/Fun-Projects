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

def create_dataframe(user_list):
    df = pd.DataFrame(user_list,columns=["Author"])
    #Which user wrote a short idea
    short_position = list(df[df["Author"].str.contains("Short")].index.array)
    df["LongShort"] = "long"
    df.loc[short_position,"LongShort"] = "short"
    df["Author"] = df["Author"].str.extract('BY (.*)')
    df["Author"] = df["Author"].str.extract('^([\w\-]+)')
    print(df)

user_list = extract_user(data)
create_dataframe(user_list)