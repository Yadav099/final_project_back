import app
from app import app
from flask import request
import json




def signup_add_user(user_data):
    teacher = {
        "teacher_name": user_data['username'],
        "teacher_email": user_data['userEmail'],
        "teacher_pass": user_data['userPassword'],
        "teacher_id": user_data['userId'],
    }
    print(teacher)
    return "done"