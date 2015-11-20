class Config(object):
    DEBUG = False
    VERSION = '1.0'
    API_ROOT_PATH = '/pykanban/v' + VERSION
    SECRET_KEY = 'YourSecretKey'
    GITHUB = {
        'consumer_key': 'GithubClientID',
        'consumer_secret': 'GithubClientSecret'
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    APP_HOST = 'http://127.0.0.1:5000'
    MONGO_HOST = 'mongodb://127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DB = 'pykanban'
    MONGO_USERNAME = ''
    MONGO_PASSWORD = ''