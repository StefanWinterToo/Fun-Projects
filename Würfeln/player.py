import pandas as pd

players = {'Name': ['Stefan', 'Sabrina']}
df = pd.DataFrame(players)

def get_player(x):
    return(df["Name"][x])