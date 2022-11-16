"""Initialize and configs"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:0308110299Go@localhost/labsaledb?charset=utf8mb4'
db = SQLAlchemy(app=app)

