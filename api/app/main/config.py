import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@localhost:{port}/customer_info'.format(username='postgres', password='test@#!451aAS', port=5432)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@customerinfo-db:{port}/customer_info'.format(username='postgres', password='test@#!451aAS', port=5432)
    

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)