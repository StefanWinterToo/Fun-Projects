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

user_list = extract_user(data)

#%%
regex = re.compile(r'\w{*}(•)')
selected_files = list(filter(regex.search, data))

# %%
company_position = []
for i in range(len(data)):
    if bool(re.search("•\s*\w*.\w*\s*•", data[i])):
        company_position.append(i)

# %%
company = list(data[i] for i in company_position)
df["Company"] = company
