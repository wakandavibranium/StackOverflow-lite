import os
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from app import db
from app import create_app
from app import models

# Get environment to run e.g development
app = create_app(config_name=os.getenv('FLASK_ENV'))

# Add Flask and Flask-SQLAlchemy instances
migrate = Migrate(app, db)

# The Manager class keeps track of all the commands and
# handles how they are called from the command line.
manager = Manager(app)

# Regitser 'db' as a migration command
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
