import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=fc3a024559a41bf4c9130f6e3345d852'
    MOVIE_API_KEY = os.environ.get(' fc3a024559a41bf4c9130f6e3345d852')
    SECRET_KEY = os.environ.get('1234')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #email configurations
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}