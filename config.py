"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    API_KEY1 = environ.get('API_KEY1')
    API_KEY2 = environ.get('API_KEY2')

class ProdConfig(Config):
    TESTING = False
    DEBUG = False

class DevConfig(Config):
    TESTING = True
    DEBUG = True  
