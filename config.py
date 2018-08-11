import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'defaultApplication'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig
}