import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def create_event(user_id, event_name, event_type, event_date, event_time, event_location, event_description, event_user_feeling, empfehlung):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO events 
        (event_user_id, event_name, event_type, event_date, event_time, event_location, event_description, event_user_feeling, event_ki_emp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, event_name, event_type, event_date, event_time, event_location, event_description, event_user_feeling, empfehlung))
    conn.commit()
    conn.close()

def get_all_events():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    connection.close()
    return events

def get_event_by_id(event_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = cursor.fetchone()
    connection.close()
    return event

def update_event(id, event_user_id, event_name=None, event_type=None, event_date=None, event_time=None, event_location=None, event_description=None):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    updates = []
    params = []

    if event_name:
        updates.append("event_name = ?")
        params.append(event_name)
    if event_user_id:
        updates.append("event_user_id = ?")
        params.append(event_name)
    if event_type:
        updates.append("event_type = ?")
        params.append(event_type)
    if event_date:
        updates.append("event_date = ?")
        params.append(event_date)
    if event_time:
        updates.append("event_time = ?")
        params.append(event_time)
    if event_location:
        updates.append("event_location = ?")
        params.append(event_location)
    if event_description:
        updates.append("event_description = ?")
        params.append(event_description)

    params.append(id)
    cursor.execute(f"UPDATE events SET {', '.join(updates)} WHERE id = ?", params)
    connection.commit()
    connection.close()

def delete_event(event_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    connection.commit()
    connection.close()





