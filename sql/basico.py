import sqlite3
# Configurar la base de datos
DATABASE = 'data.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                distance REAL,
                time INTEGER,
                date TEXT
            )
        ''')
        conn.commit()

def insert_data(distance,time,date,):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''  
            INSERT INTO records (distance, time, date)
            VALUES (?, ?, ?);
        ''', (distance, time, date))
        conn.commit()

def get_all_data_desc():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM records ORDER BY ID DESC;')
        records = cursor.fetchall()
    return records

def get_all_data_asc():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM records ORDER BY ID ASC;')
        records = cursor.fetchall()
    return records

def delete_last():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM records WHERE ID = (SELECT ID FROM records ORDER BY ID DESC LIMIT 1);')
        conn.commit()