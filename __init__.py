from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy model
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'sheepfarm'
    app.config['SQLALCHEMY_DATABASE_URL'] =  'sqlite:///db.sqlite'
    
    db.init_app(app) 