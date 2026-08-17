import sqlite3 as sq
from pathlib import Path

def insert_user(database, username, password, email, age):

    conn = sq.connect(database)
    corsur = conn.cursor()
    
    corsur.execute("""
    INSERT INTO users 
    (username, password_hash, email, age)
    VALUES(?,?,?,?)"""
    ,(username, password, email, age))
    
    conn.commit()
    conn.close()
    
    print("User inserted succusfully!")
    
    
    
    
    
    
    
    
# username = input("Enter USERNAME: ")
# password = input("please enter  your password: ")
# email = input("Enter EMAIL: ")
# age = int(input("Enter AGE: "))