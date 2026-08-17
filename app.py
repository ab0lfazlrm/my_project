from flask import Flask, render_template, request
import sqlite3 as sq

from database import database
from users import insert_user



app = Flask(__name__)


def get_db_connection():
    conn = sq.connect(database)
    conn.row_factory = sq.Row
    return conn



@app.route("/")
def home():
    conn = get_db_connection()
    
    users = conn.execute("""SELECT id, username, email, age FROM users""").fetchall()
    
    conn.close
    return str([dict(user) for user in users])


@app.route("/templates/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        
        insert_user(database, username, password, email,  age)
        
        return ("<p>user registered succesfully!</p>")
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)