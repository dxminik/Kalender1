import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# USER ERSTELLEN VORLAGE
#c.execute("CREATE TABLE IF NOT EXISTS user (user_id INTEGER PRIMARY KEY,"
#          "user_name TEXT NOT NULL,"
#          "user_surname TEXT NOT NULL,"
#          "user_sex TEXT NOT NULL, "
#          "user_birthday TEXT NOT NULL)")
c.execute("""
    ALTER TABLE user ADD COLUMN user_interests TEXT
""")
conn.commit()
conn.close()
