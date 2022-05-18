from flask import Flask

app = Flask(__name__)

app.secret_key = "SHHHHHHHH"
DATABASE = "recipe_db"