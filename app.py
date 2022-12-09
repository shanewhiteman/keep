from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

SECRET_KEY = 'masterkey'

#instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)

# import declared routes
import routes, models

with app.app_context():
    # create tables that do not exist
    db.create_all()

