from flask_ngrok import run_with_ngrok
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY']="Secret"
app.debug = True
CORS(app)
jwt=JWTManager(app)
run_with_ngrok(app)
from app import routes
