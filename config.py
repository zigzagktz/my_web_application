from dotenv import load_dotenv
from os import environ, path
import datetime

load_dotenv('.env')

class configuration:
    SECRET_KEY = environ.get('SECRET_KEY')
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=int(environ.get('PERMANENT_SESSION_LIFETIME')))


