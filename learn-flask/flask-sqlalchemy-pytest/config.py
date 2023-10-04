class Config:
    ...

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.sqlite'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.sqlite'

class ProductionConfig(Config):
    ...

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}