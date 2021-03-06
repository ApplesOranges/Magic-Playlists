from decouple import config

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:teemo230@localhost:5432/magic-playlists"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL_REAL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configdic = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}