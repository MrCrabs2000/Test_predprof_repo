from flask import render_template
from database.db_session import init_database

from configs.configs import app
from routs.routs import register_all_blueprints


register_all_blueprints(app)


@app.route('/')
def main():
    return render_template('')


if __name__ == '__main__':
    app.run(debug=True)