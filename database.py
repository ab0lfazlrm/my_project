import sqlite3 as sq
from pathlib import Path

# مشخص کردن مسیر و نام دیتا بیس
folder = Path(__file__).resolve().parent
database = folder / "users.db"


# ساخت دیتا بیس
def create_database(data_base):
    conn = sq.connect(data_base)
    conn.close()
    print("Database created successfully")

# *******************************************
# ساخت tables
def create_tables(data_base):
    conn = sq.connect(data_base)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()

# در صورت عدم وجود دیتا بیس یک دیتا بیس جدید بسازیم
if not database.exists():
    create_database(database)
create_tables(database)
    
    

