from src import create_app,db
 
# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg
# to run using windows
# SET FLASK_APP=main.py
# SET FLASK_ENV=development to enable reload
# flask run --reload for testing. remove --reload for production
# app = create_app()

db.create_all(app=create_app())