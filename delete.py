from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)


@app.route("/")
def list():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    cur.execute("Select * from person")
    rows = cur.fetchall()
    return render_template("delete.html", rows=rows)


@app.route("/testdelete", methods=["GET", "POST"])
def testdelete():
    conn = mysql.connect(user="abcd", password="1234", database="Emp")
    cur = conn.cursor()
    id = request.form["id"]
    print(id)
    cur.execute("DELETE from person WHERE id='{}';".format(id))
    conn.commit()
    return render_template("message.html", msg="data has been deleted")


@app.route("/backhome")
def backhome():
    return render_template("student.html")


if __name__ == "__main__":
    app.run(debug=True)

