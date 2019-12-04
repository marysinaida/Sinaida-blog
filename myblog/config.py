import os


class Config:
    '''
    General configuration class
    '''
    SECRET_KEY='snydmary'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/test'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
class ProdConfig(Config):
    '''
    Production configuration class
    '''
    
    pass
class DevConfig(Config):
    '''
    Development configuration class
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True
config_options = {
    'production': ProdConfig,
    'development':DevConfig
}
   