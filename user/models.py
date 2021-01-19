from flask import Flask, jsonify, request, render_template, redirect, flash, url_for
from passlib.hash import pbkdf2_sha256
import uuid
import user_database

class User:
    
    def __init__(self):
        self._id = uuid.uuid4().hex
        self.name = request.form.get('name')
        self.email = request.form.get('email')
        self.password = pbkdf2_sha256.encrypt(request.form.get('password'))
        
    def signup(self):
        
        user = {
            "_id": self._id, 
            "name": self.name,
            "email": self.email, 
            "password": self.password
        }
        
        return user_database.add_user(user)
    
    def login(self):
        pass
    
    def logout(self):
        pass
