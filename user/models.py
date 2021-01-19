from flask import Flask, jsonify, request, render_template, redirect, flash, url_for, session
from passlib.hash import pbkdf2_sha256
import uuid
import user_database


class User:


    def signup(self):
        """Signs a user up by creating a new entry to the database. Main use
        is with the registration page.
        """
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": pbkdf2_sha256.encrypt(request.form.get('password'))
        }

        # Check for duplicate entries
        if user_database.check_for_user(user["email"]):
            return False
        else:
            user_database.add_user(user)
            return True


    def login(self, user):
        """Checks for the passed in user on database and assigns a session for them accordignly.

        Keyword arguments:
        user -- The user to be authenticated
        """

        # Checks for user in database
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def logout(self):
        pass
