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

def get_data_by_date_range(start_date, end_date):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM records WHERE date BETWEEN ? AND ? ORDER BY ID ASC', (start_date, end_date))
        records = cursor.fetchall()
    return records

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

def calculate_average_speed(total_distance, total_minutes):
    if total_minutes == 0:
        return 0
    return round((total_distance / total_minutes) * 60, 2)

def total_sums(records):
    total_distance = round(sum(row[1] for row in records),2)
    total_minutes = round(sum(row[2] for row in records),2)
    return total_distance, total_minutes