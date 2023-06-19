from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://megan:mego@localhost/mydatabase'
app.config['SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import views
