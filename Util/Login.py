from datetime import datetime, timedelta

import jwt

import app
from app import app
from flask import request, jsonify
import json
from flask_jwt_extended import create_access_token


def Login_validate(teacher):
    if teacher["userEmail"] == "yadav":
        encoded = jwt.encode({'exp': datetime.utcnow() + timedelta(seconds=30), 'a': 't'}, 'secret',
                             algorithm='HS256').decode(
            "utf-8")
        print(type(encoded))
        result = jsonify({"token": str(encoded), "loggedIn": 'true'})


    else:

        result = jsonify({"error": "Invalid user"})

        # login data in dictionary format got from routes.py
    return result
