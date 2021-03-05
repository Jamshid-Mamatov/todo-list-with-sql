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
        
        return f"{self.id}. {self.task}   {self.state}"


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
    return "task add"


@app.route("/remove")

def remove():
    tasks=User_task.query.all()
    content="task remove"
    total=""
    for task in tasks:
        total+=(str(task)+'\n')
    print(total)
    return render_template("remove.html",content=content,total=total)
    
@app.route("/rem",methods=["POST"])

def remove_task():
    r=request.form
    rem_num=r.get("remove_num")
    if rem_num!=None:
        user=User_task.query.get(rem_num)
        db.session.delete(user)
        db.session.commit()
    return "ok"


@app.route("/update")
def updates():
    content="update task"
    tasks=User_task.query.all()
    total=""
    for task in tasks:
        total+=(str(task)+'\n')
    return render_template("update.html",content=content,total=total)

@app.route("/upd",methods=["POST"])

def task_update():
    r=request.form
    task=r.get("task","")
    number=r.get("number","")
    state=r.get("state","")
    user=User_task.query.get(number)
    if task!="":
        user.task=task
    if state!="":
        user.state=state
    
    db.session.commit()
    return "ok"
        
    


if __name__=="__main__":
    app.run(debug=True)