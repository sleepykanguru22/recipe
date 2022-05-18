from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "SHHHHHHHH"

bcrypt = Bcrypt(app)
DATABASE = "recipe_db"