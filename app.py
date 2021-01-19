from flask import Flask, render_template, request, redirect, flash, url_for, session
from user.models import User
import os
import user_database
from user_database import db


app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    # Handles a user signup
    if(request.method == 'POST'):
        user = User()
        user.signup()
        if(user_database.check_for_user(user._id)):
            flash('Your account was created succesfully!', "success")
            return redirect('/login')  
        else:
            flash('Your account could not be created succesfully! Please check input and try again.', "error")
            return redirect('/register')      
        
    # Default GET route
    return render_template('register.html')

@app.route('/login', methods = ['GET'])
def login():
    return render_template('login.html')


@app.route('/logout', methods= ['GET,POST'])
def logout():
    return 'Logout'
    

if __name__ == '__main__':
    app.run(debug= True)