import pandas as pd
import numpy

data = {'Name': ["Hans", "Markus", "Stefan"],
        "Age": [23, 24, 12]}

df = pd.DataFrame(data)
print(df)

print("")

print(df.loc[:,"Name"].values.tolist())
print(df.loc[:,"Name"].values.tolist().__class__)

print("")

print(df.sort_values("Age", ascending=False))

print("")

print(df.columns.values)

