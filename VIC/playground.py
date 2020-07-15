#%%
import pandas as pd
import numpy as np
from itertools import combinations
import re

#%%
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
    #
    df = pd.DataFrame(user_list,columns=["Author"])
    #Which user wrote a short idea
    short_position = list(df[df["Author"].str.contains("Short")].index.array)
    df["LongShort"] = "long"
    df.loc[short_position,"LongShort"] = "short"
    df["Author"] = df["Author"].str.extract('BY (.*)')
    df["Author"] = df["Author"].str.extract('^([\w\-]+)')
    df = df[df["Author"].isna() == False]
    return(df)

def extract_company(l):
    company_position = []
    for i in range(len(l)):
        if bool(re.search("•\s*\w*(.|,)*\w*\s*•", l[i])):
            company_position.append(i)
    return(company_position)

def append_company_dataframe(l, df):
    company = []

    for i in l:
        company.append(data[i])
    df["Company"] = company
    df["Mcap"] = df["Company"].str.extract('((((\$|€)\d*(,|.)\d*\w*)))')[0]
    df["Price"] = df["Company"].str.extract('(?<=\•)(.*?)\•')
    df["Company"] = df["Company"].str.extract('^(.+?)•')
    df["Ticker"] = df["Company"].str.extract('(\w+|\w+\.\w+)\W*$')
    for i in range(len(df)):
        df["Company"][i] = re.sub(r'(\w+|\w+\.\w+)\W*$',' ',df["Company"][i])
    return(df)

user_list = extract_user(data)
df = create_dataframe(user_list)
company_list = extract_company(data)
df = append_company_dataframe(company_list, df)

# %%
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
df["Date"] = ""

for i in range(len(data)):
    if bool(re.search("•\s*\w*(.|,)*\w*\s*•", data[i])):
        if any(day in data[i-1] for day in days) == True:
            foo_list_company = []
            foo_list_company.append(data[i])
            #if(any(x in foo_list for x in company_list)):
                #print(i)
            foo_list_date = []
            foo_list_date.append(data[i-1])
            #print(data[i-1])

            foo = {"Company": foo_list_company, "Date": foo_list_date} 

            c_df = pd.DataFrame(foo)
            #c_df["Date"] = foo_list_date
            c_df["Mcap"] = c_df["Company"].str.extract('((((\$|€)\d*(,|.)\d*\w*)))')[0]
            c_df["Mcap"] = c_df["Mcap"][0]
            c_df["Price"] = c_df["Company"].str.extract('(?<=\•)(.*?)\•')
            c_df["Price"] = c_df["Price"][0]
            c_df["Company"] = c_df["Company"].str.extract('^(.+?)•')
            c_df["Company"] = c_df["Company"][0]
            c_df["Ticker"] = c_df["Company"].str.extract('(\w+|\w+\.\w+)\W*$')
            c_df["Ticker"] = c_df["Ticker"][0]
            #print(df.where(df["Ticker"]==c_df["Ticker"][0]))
            print(type(c_df["Ticker"]))
            
            
            
            
# %%
