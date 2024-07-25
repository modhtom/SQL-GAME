from db import *
from flask import (
    Flask,
    request,
    redirect,
    render_template,
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = "T&v$2PQsLsagffsdfas4534&^&*(8Rk@5gFw#ZmDp1YhCn*4uXy7eBdAa6VbGz3JqU"
limiter = Limiter(
    app=app, key_func=get_remote_address, default_limits=["50 per minute"]
)


@app.route("/", methods=["GET"])
def root_dir():
    return redirect("/home")


@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/execute', methods=['POST'])
def execute():
    query = request.form['query']
    result = ''
    try:
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.commit()
        conn.close()
        
        if rows:
            result = '<table border="1"><tr>'
            for column in columns:
                result += f'<th>{column}</th>'
            result += '</tr>'
            for row in rows:
                result += '<tr>'
                for cell in row:
                    result += f'<td>{cell}</td>'
                result += '</tr>'
            result += '</table>'
        else:
            result = 'No results found.'
    except Exception as e:
        result = str(e)
    
    return render_template('home.html', result=result, query=query)


@app.route('/guess', methods=['POST'])
def Guess():
    guess_name = request.form['Guess'].strip()
    result = ''
    
    try:
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT IsCorrect 
            FROM Solutions 
            WHERE GuestName is ?;
        """, (guess_name,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            is_correct = row[0]
            if is_correct:
                result = "Congrats, you found the brains behind the murder!"
            else:
                result = "That's not the right person. Try again!"
        else:
            result = "No such person found. Please try again with a valid name."
    
    except Exception as e:
        result = str(e)
    
    return render_template('home.html', result2=result)

if __name__ == "__main__":
    game()
    app.run(host="0.0.0.0", debug=True)