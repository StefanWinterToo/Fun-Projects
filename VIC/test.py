#%%#
from Converter import open_file, extract_user, extract_company, create_dataframe, append_company_dataframe, replace_mcap 

data = open_file()
user_list = extract_user(data)
df = create_dataframe(user_list)
company_list = extract_company(data)
df = append_company_dataframe(company_list, df, data)
print(df)

# %%
print(df)

# %%
