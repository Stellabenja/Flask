from datetime import datetime

from flask_pymongo import PyMongo
import bcrypt as bcrypt
from flask import Flask, render_template, request
from mongoengine import connect

from User import User
from registerForm import register

app = Flask(__name__, template_folder='templates')
app.secret_key = 'development key'
app.config['MONGO_URI']="mongodb://localhost:27017/Person"
app.config['MONGO_DBNAME']="Person"
mongo=PyMongo(app)

connect('Person',host='localhost',port=27017)
@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/login')
def login():

    return 'hello_world'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = register()
    if request.method == 'POST':
         user= mongo.db.Person
         existing_user = user.find_one({'email': request.form['email']})

         if existing_user is None:
             password=request.form.get('password')
             confirmPassword=request.form.get('confirm')
             if len(password) >=6 :
                 if password is not confirmPassword:
                      user = User(
                       firstname=request.form.get("firstname"),
                       lastname=request.form.get("lastname"),

                       birthdate=datetime.strptime(request.form.get("birthdate"), '%Y-%m-%d'),
                       email=request.form.get("email"),
                       password=bcrypt.hashpw(request.form.get("password").encode('utf-8'), bcrypt.gensalt())

                        )
                      user.save()
                 return 'Passwords must match!'
             return 'Passwords length must greater than 5!'
         return 'That username already exists!'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
