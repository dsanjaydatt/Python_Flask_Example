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
            conn = mysql.connect(user="ghost", password="1234", database="Emp")
            cur = conn.cursor()
            sql = "INSERT INTO person(name,roll)values('{}','{}')".format(name, roll)
            cur.execute(sql)
            conn.commit()
            msg = "Data Successfully stored"
            return render_template("message.html", msg=msg)
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    app.run(debug=True)

