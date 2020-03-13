import sqlite3, pandas as pd, numpy as np

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
df = pd.read_sql("""SELECT * FROM users""", conn)
usernames = df['nickname']
print(len(df.nickname.loc[df.nickname == 'worldwidehomeboy']))