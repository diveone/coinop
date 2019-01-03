"""
CONFIGURATION
=============
****************************************************************
     SENSITIVE CREDENTIALS ARE **NEVER** TO BE STORED HERE.
****************************************************************

Basic settings common to all applications live here. For local:
* Open config/dev.py
* Modify or add any settings
* Add env variable: APP_CONFIG_FILE=/path/to/config/dev.py
"""
from coinop.settings.common import *

SECRET_KEY = 'secretzzz'
DEBUG = True

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'coinop.log'
LOGGING_LEVEL = logging.DEBUG

DB_NAME = os.getenv('DB_COINOP', 'coinop')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PWD = os.getenv('DB_PASSWORD', 'admin')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD,
                                                               DB_HOST, DB_PORT,
                                                               DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

COINAPI_KEY = os.getenv('COINOP_API_KEY', '')
COINAPI_URL = os.getenv('COINOP_URL')
