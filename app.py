from flask import Flask, request, url_for,render_template
from flask_pymongo import PyMongo,MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client["register"]
users=db["users"]


@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def reg():
    return render_template('register.html')



if __name__=="__main__":
    app.run(debug=True)