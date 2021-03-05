from app import db
from flask import Flask
from app import User_task
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

@app.route("/add")

def add():
    task1=User_task(task="homework",state="False")
    task2=User_task(task="work",state="False")

    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()
    return "hello tasks"

if __name__=="__main__":
    app.run(debug=True)
