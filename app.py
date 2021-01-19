from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta
from user.models import User
import os
import user_database as db

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def home():
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect('/login')

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
            flash('User email already in use.' , "error")
            return redirect('/register')      
        
    # Default GET route
    return render_template('register.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    # Handles a user login
    if(request.method == 'POST'):
        user = User()
        success_flag = user.login()
        
        if(success_flag):
            flash('Your were logged in succesfully!', "success")
            return redirect('/')
        else:
            flash('Error logging in', 'error')
            return redirect('/login')
    
    # Default GET route
    return render_template('login.html')


@app.route('/logout')
def logout():
    # handles a user logout
    try:
        user = User()
        success_flag = user.logout()
        if success_flag:
            flash('Your were logged out succesfully!', "success")
            return redirect(url_for('login'))
    except:
        flash("You are not logged in", "warning")
        return redirect(url_for('login'))
            
if __name__ == '__main__':
    app.run(debug= True)