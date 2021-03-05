from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db=SQLAlchemy(app)

class User_task(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(80),unique=True)
    state=db.Column(db.String())
    def __str__(self) -> str:
        
        return self


@app.route("/")
def home(): 

    return "hello"

@app.route("/add")
def add_task():
    task1=User_task(task="homework",state="False")
    task2=User_task(task="work",state="False")

    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()
    return "hello world"

if __name__=="__main__":
    app.run(debug=True)