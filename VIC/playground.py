#%%
import pandas as pd
import numpy as np
from itertools import combinations
import re
from datetime import datetime

#%%
file = open("vic.txt", "r")
data = file.read()
file.close()
data = data.split("\n")

def extract_user(l):
    user_position = []
    for i in range(len(l)):
        if bool(re.search("^BY ", l[i])):
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
    df = df[df["Author"].isna() == False]
    return(df)

def extract_company(l):
    company_position = []
    for i in range(len(l)):
        if bool(re.search("•\s*\w*(.|,)*\w*\s*•", l[i])):
            if bool(re.search("^((?!Short Idea).)*$", l[i])):
                # Excludes wrongly extracted users (BY pcm983 • Short Idea • Reactivate)
                company_position.append(i)
    return(company_position)


def append_company_dataframe(l, df):
    company = []
    foo_list_date = []
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    for i in l:
        if any(day in data[i-1] for day in days) == True:
            company.append(data[i] + "_&CONCATENATE&_" + data[i-1])
        else:
            company.append(data[i] + "_&CONCATENATE&_" + "")

    df["Company"] = company
    df[["Company", "Date"]] = df["Company"].str.split("_&CONCATENATE&_", expand = True)
    df["Date"] = df["Date"].replace("", np.NaN)
    df["Date"] = df["Date"].fillna(method = "ffill")
    df["Date"] = df["Date"].apply(lambda x: datetime.strptime(x, "%A, %b %d, %Y"))
    df["Mcap"] = df["Company"].str.extract('((((\$|€)\d*(,|.)\d*\w*)))')[0]
    df["Price"] = df["Company"].str.extract('(?<=\•)(.*?)\•')
    df["Company"] = df["Company"].str.extract('^(.+?)•')
    df["Ticker"] = df["Company"].str.extract('(\w+|\w+\.\w+)\W*$')
    for i in range(len(df)):
        df["Company"][i] = re.sub(r'(\w+|\w+\.\w+)\W*$',' ',df["Company"][i])
    return(df)

def replace_mcap(df):
    df["Mcap"] = df["Mcap"].str.replace('mn', ',000,000')

user_list = extract_user(data)
df = create_dataframe(user_list)
company_list = extract_company(data)
df = append_company_dataframe(company_list, df)
replace_mcap(df)
print(df)


# %%
