# Third-party imports
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# Local imports
from instance.config import app_config

# Create an instance of SQLAlchemy
db = SQLAlchemy()


def create_app(config_name):
    # Create an instance of Flask
    app = FlaskAPI(__name__, instance_relative_config=True)

    # Get the environment to run our flask app e.g development
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect to our database
    db.init_app(app)

    return app
