from flask import Flask,render_template,request
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
    content="todo list"
    return render_template("home.html",content=content)


@app.route("/create")

def create_list():

    content="create to do list"
    return render_template("create.html",content=content)



@app.route("/add")
def add_task():
    content="add task"
    
    return render_template("add.html",content=content)

@app.route("/formAdd",methods=["POST","GET"])
def get_add():
    r=request.form
    task_get=r.get("task")
    # print(task_get)
    if task_get!=None:
        task1=User_task(task=task_get,state="False") 
        
        db.session.add(task1)
        db.session.commit()
    return "worked"


if __name__=="__main__":
    app.run(debug=True)