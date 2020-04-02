import jwt
from flask import request,Response

from Util.Dashboard import video_converter
from Util.Login import Login_validate
from Util.Signup import signup_add_user
from app import app


@app.route("/", methods=['GET'])
def home():
    return "fuck you saurabh"

@app.route("/Signup", methods=['POST'])
def Signup():
    data = request.json
    return signup_add_user(data)



@app.route("/Login", methods=['POST'])
def Login():
    # print(request.authorization.username)
    if request.authorization :
        # and request.authorization.username and request.authorization.password:

        return Login_validate({

            "userEmail": request.authorization.username,
            "password": request.authorization.password
        })
    else:

        return "wrong"


@app.route("/Dashboard", methods=['POST'])
def Video_uploader():

    try:
        encode = jwt.decode(request.headers['Authorization'], 'secret', algorithms=['HS256'])
        if encode:
            print(encode)
        else:
            print("No")
    except Exception as e:
        print(e)
    # print(data)
    # return video_converter(request.files['Video'])
    return "done"