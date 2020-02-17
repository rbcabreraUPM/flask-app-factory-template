from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize db
db = SQLAlchemy()


#import blueprint routes here 
from src.students.routes import student_bp

def create_app(config_filename=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
    app.config['SECRET_KEY '] = 'GGWP MGA SIRS'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    

    #register blueprints
    app.register_blueprint(student_bp)
    return app