from flask import (
    Flask,
    request,
    redirect,
    render_template,
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3
from db import game as game1
from db2 import game as game2

app = Flask(__name__)
app.secret_key = "T&v$2PQsLsagffsdfas4534&^&*(8Rk@5gFw#ZmDp1YhCn*4uXy7eBdAa6VbGz3JqU"
limiter = Limiter(
    app=app, key_func=get_remote_address, default_limits=["50 per minute"]
)

@app.route("/", methods=["GET"])
def root_dir():
    return render_template("index.html")

@app.route("/case1", methods=["GET"])
def case1_home():
    return render_template("home.html")

@app.route("/case2", methods=["GET"])
def case2_home():
    return render_template("home2.html")

def execute_query(query, db_name):
    result = ""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            columns = [description[0] for description in cursor.description]
            result = '<table border="1"><tr>'
            for column in columns:
                result += f"<th>{column}</th>"
            result += "</tr>"
            for row in rows:
                result += "<tr>"
                for cell in row:
                    result += f"<td>{cell}</td>"
                result += "</tr>"
            result += "</table>"
        else:
            result = "No results found."
        conn.close()
    except Exception as e:
        result = str(e)
    return result

@app.route("/execute_case1", methods=["POST"])
def execute_case1():
    query = request.form["query"]
    result = execute_query(query, "game.db")
    return render_template("home.html", result=result, query=query)

@app.route("/execute_case2", methods=["POST"])
def execute_case2():
    query = request.form["query"]
    result = execute_query(query, "game2.db")
    return render_template("home2.html", result=result, query=query)

def check_guess(guess_name, db_name):
    result = ""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT IsCorrect FROM Solutions WHERE GuestName = ?;", (guess_name,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            if row[0]:
                result = "Congrats, you found the brains behind the murder!"
            else:
                result = "That's not the right person. Try again!"
        else:
            result = "No such person found. Please try again with a valid name."
    except Exception as e:
        result = str(e)
    return result

@app.route("/guess_case1", methods=["POST"])
def guess_case1():
    guess_name = request.form["Guess"].strip()
    result = check_guess(guess_name, "game.db")
    return render_template("home.html", result2=result)

@app.route("/guess_case2", methods=["POST"])
def guess_case2():
    guess_name = request.form["Guess"].strip()
    result = check_guess(guess_name, "game2.db")
    return render_template("home2.html", result2=result)

if __name__ == "__main__":
    game1()
    game2()
    app.run(host="0.0.0.0")