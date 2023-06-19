from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://megan:mego@localhost/mydatabase'
app.config['SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app import views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
