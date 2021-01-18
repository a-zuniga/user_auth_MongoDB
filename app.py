from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!!"

@app.route('/')

@app.route('/login')
def login():
    return "Login"

@app.route('/logout')
def logout():
    return "Logout"
    

if __name__ == '__main__':
    app.run(debug= True)