from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)


@app.route("/")
def list():
    conn = mysql.connect(user="root", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select * from person")
    rows = cur.fetchall()
    return render_template("show.html", rows=rows)


@app.route("/testupdate", methods=["GET", "POST"])
def testupdate():
    conn = mysql.connect(user="root", password="1234", database="Emp")
    cur = conn.cursor()
    name = request.form["name"]
    roll = request.form["roll"]
    print(roll)
    print(name)
    cur.execute("UPDATE person set roll='{}' where name='{}'".format(roll, name))
    cur.execute("UPDATE person set name='{}' where roll='{}'".format(name, roll))
    conn.commit()
    return render_template("message.html", msg="data updated")


@app.route("/backhome")
def backhome():
    return render_template("student.html")

if __name__ == "__main__":
    app.run(debug=True)

