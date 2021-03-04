from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db=SQLAlchemy(app)

class User_task():
    id= db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(80),unique=True)
    state=db.Column(db.String(20))


@app.route("/")
def home():

    return "hello"

if __name__=="__main__":
    app.run(debug=True)