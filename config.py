import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'ENTER_YOUR_PASSWORD'
    MYSQL_DB = 'api_app'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_BINDS = {
    'db1': SQLALCHEMY_DATABASE_URI,
    'db2': ''
}
 
