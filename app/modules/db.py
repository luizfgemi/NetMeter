import sqlite3
from .config import db_path

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        download_speed REAL,
        upload_speed REAL,
        ping REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')

    conn.commit()
