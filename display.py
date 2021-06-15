from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)


@app.route("/")
def list():
    conn = mysql.connect(user="ghost", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select * from person")
    rows = cur.fetchall()
    return render_template("display.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

