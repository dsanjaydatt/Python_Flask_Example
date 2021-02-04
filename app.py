from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)


@app.route("/")
def student():
    return render_template("student.html")


@app.route("/act", methods=["GET", "POST"])
def act():
    if request.method == "POST":
        try:
            name = request.form["name"]
            roll = request.form["roll"]
            conn = mysql.connect(user="abcd", password="1234", database="Emp")
            cur = conn.cursor()
            sql = "INSERT INTO person(name,roll)values('{}','{}')".format(name, roll)
            cur.execute(sql)
            conn.commit()
            return render_template("output.html", msg="Data has been stored")
        except:
            return "Database connection error"


@app.route("/display")
def display():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select * from person")
    rows = cur.fetchall()
    return render_template("display.html", rows=rows)


@app.route("/update")
def list():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select * from person")
    rows = cur.fetchall()
    return render_template("show.html", rows=rows)


@app.route("/testupdate", methods=["GET", "POST"])
def testupdate():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    name = request.form["name"]
    roll = request.form["roll"]

    cur.execute("UPDATE person set roll='{}' where name='{}'".format(roll, name))
    cur.execute("UPDATE person set name='{}' where roll='{}'".format(name, roll))
    conn.commit()
    return render_template("output.html", msg="Data updated")


@app.route("/delete")
def list1():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select* from person")
    rows = cur.fetchall()
    return render_template("delete.html", rows=rows)


@app.route("/testdelete", methods=["GET", "POST"])
def testdelete():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    id = request.form["id"]
    print(id)
    cur.execute("DELETE FROM person WHERE id ='{}';".format(id))
    conn.commit()
    return render_template("output.html", msg="Data Deleted")


@app.route("/backhome")
def backhome():
    return render_template("student.html")


if __name__ == "__main__":
    app.run(debug=True)

