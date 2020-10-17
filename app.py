from flask import Flask, request, url_for,render_template
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
    if request.method =='POST':
        user=request.form['username']
        password=request.form['password']
        correctpw=verifypw(user,password)
        if correctpw:
            return render_template('home.html')
        else:
            return render_template('login.html')

    else:
        return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def reg():
    if request.method =='POST':
        user=request.form['username']
        email=request.form['mail']
        password=request.form['password']
        verify=verifyuser(user)
        if verify:
            users.insert_one({'Username':user,'Email':email,'Password':password})
            return render_template('login.html')
        else:
            return render_template('register.html')


    else:
        return render_template('register.html')



if __name__=="__main__":
    app.run(debug=True)