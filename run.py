# Third-party imports
import os

# Local imports
from app import create_app

# Get the environment settings we setup earlier.In this case it's "development"
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
