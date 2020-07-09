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
    return(df)

def extract_company(l):
    company_position = []
    for i in range(len(l)):
        if bool(re.search("•\s*\w*(.|,)*\w*\s*•", l[i])):
            company_position.append(i)
    return(company_position)

def append_company_dataframe(list, df):
    company = []

    for i in list:
        company.append(data[i])

    df["Company"] = company
    return(df)

user_list = extract_user(data)
df = create_dataframe(user_list)
company_list = extract_company(data)
df = append_company_dataframe(company_list, df)

# Extract Mcap
df["Mcap"] = df["Company"].str.extract('((((\$|€)\d*(,|.)\d*\w*)))')[0]
df["Price"] = df["Company"].str.extract('(?<=\•)(.*?)\•')
df["Company"] = df["Company"].str.extract('^(.+?)•')
print(df)