from flask import Flask, request, url_for,render_template,flash,redirect
from flask_pymongo import PyMongo,MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client["register"]
users=db["users"]

def verifypw(user, password):
    pw=users.find({'Username':user})[0]['Password']
    if pw == password:
        return True
    else:
        return False

def verifyuser(username ):
    if users.find({'Username':username}).count()==0:
        return True
    else:
        return False

@app.route('/',methods=['GET','POST'])
def login():
    error=None
    if request.method =='POST':
        user=request.form['username']
        password=request.form['password']
        correctpw=verifypw(user,password)
        if correctpw:
            return redirect(url_for('home'))
        else:
            error="Invalid Username or Password"
            return render_template('login.html', error=error)
    else:
        error=None
        return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def reg():
    error=None
    if request.method =='POST':
        user=request.form['username']
        email=request.form['mail']
        password=request.form['password']
        verify=verifyuser(user)
        if verify:
            users.insert_one({'Username':user,'Email':email,'Password':password})
            return redirect(url_for('login'))
        else:
            error="Username already exist"
            return render_template('register.html',error=error)


    else:
        error=None
        return render_template('register.html')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)