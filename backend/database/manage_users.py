import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def create_user(user_name, user_surname, user_sex, user_birthday, user_interests):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO user 
        (user_name, user_surname, user_sex, user_birthday, user_interests)
        VALUES (?, ?, ?, ?, ?)
    """, (user_name, user_surname, user_sex, user_birthday, user_interests))
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user

def update_user(user_id, user_name=None, user_surname=None, user_sex=None, user_birthday=None, user_interests=None):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    updates = []
    params = []

    if user_id:
        updates.append("event_name = ?")
        params.append(user_id)
    if user_id:
        updates.append("user_name = ?")
        params.append(user_name)
    if user_surname:
        updates.append("user_surname = ?")
        params.append(user_surname)
    if user_sex:
        updates.append("user_sex = ?")
        params.append(user_sex)
    if user_birthday:
        updates.append("user_birthday = ?")
        params.append(user_birthday)
    if user_interests:
        updates.append("user_interests = ?")
        params.append(user_interests)


    params.append(id)
    cursor.execute(f"UPDATE user SET {', '.join(updates)} WHERE id = ?", params)
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
    connection.commit()
    connection.close()





