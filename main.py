from flask import Flask, render_template
import os

from routs.routs import register_all_blueprints
from database.db_session import init_database


app = Flask(__name__)
app.secret_key = 'secret_key'
os.makedirs('db', exist_ok=True)
init_database()

register_all_blueprints(app)


@app.route('/')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)