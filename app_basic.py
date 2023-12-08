from flask import Flask, render_template
import pathlib
import sqlite3

app = Flask(__name__)

base_path = pathlib.Path().cwd()
db_name = "Salary.db"
file_path= base_path/db_name
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    Salary=cursor.execute("SELECT *FROM salary").fetchall()
    con.close()
    return render_template("data_table_fillin.html",Salary=Salary)

if __name__ == '__main__':
    app.run(debug=True)
