import os

basedir = os.path.abspath(os.path.dirname(__name__))


class BaseConfig:
    ...


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    ...


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


config = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig,
    'Testing': TestingConfig
}
