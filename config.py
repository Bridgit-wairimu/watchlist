import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=fc3a024559a41bf4c9130f6e3345d852'
    MOVIE_API_KEY = os.environ.get(' fc3a024559a41bf4c9130f6e3345d852')
    SECRET_KEY = os.environ.get('1234')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}