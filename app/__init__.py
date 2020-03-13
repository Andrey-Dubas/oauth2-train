from flask import Flask

from dotenv import load_dotenv
import os

print(os.environ.get('CLIENT_ID'))
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.flaskenv')
load_dotenv(dotenv_path)
print(os.environ.get('CLIENT_ID'))


app = Flask(__name__)

from app import routes