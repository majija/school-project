import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users
                  (id int, nickname text, rating float
                  )
               """)
