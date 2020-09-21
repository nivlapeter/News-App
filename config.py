import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=3d407c9a7fe04a5896ba0ab421c6e2d9'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey=3d407c9a7fe04a5896ba0ab421c6e2d9'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    #SECRET_KEY = os.environ.get('SECRET_KEY')

   
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}