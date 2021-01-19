from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta
from user.models import User
import os
import user_database
from user_database import db


app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def home():
    if "user" in session:
        return render_template("home.html")
    else:
        redirect('/login')

@app.route('/register', methods=['POST', 'GET'])
def register():
    # Handles a user signup
    if(request.method == 'POST'):
        user = User()
        success_flag = user.signup()
        if(success_flag):
            flash('Your account was created succesfully!', "success")
            return redirect('/login')  
        else:
            flash("User email already in use. Please try again, error")
            return redirect('/register')      
        
    # Default GET route
    return render_template('register.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if(request.method == 'POST'):
        credentials = {
            'email' : request.get('email'),
            'password': request.get('password')
        }
    return render_template('login.html')


@app.route('/logout', methods= ['GET,POST'])
def logout():
    return 'Logout'
    

if __name__ == '__main__':
    app.run(debug= True)