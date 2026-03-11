from flask import Flask
import os

from database.db_session import init_database


app = Flask(__name__)
app.secret_key = 'secret_key'
os.makedirs('db', exist_ok=True)
init_database()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
app.template_folder = TEMPLATE_DIR
