from flask import Flask, render_template, g
import psycopg2


app = Flask(__name__)
DBNAME = "wifisteal"


def connect_db():
    conn = psycopg2.connect(database=DBNAME)
    conn.autocommit = True
    return conn


@app.before_request
def open_db():
    g.db = connect_db()
    g.cursor = g.db.cursor()


@app.route('/')
def hello_world():
    g.cursor.execute("SELECT * FROM password ORDER BY id DESC LIMIT 30")
    password = g.cursor.fetchall()
    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run()
