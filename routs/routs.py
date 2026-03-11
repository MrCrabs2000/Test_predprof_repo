from routs.auth.login import login_page
from routs.auth.logout import logout_page
from routs.auth.register import register_page



def register_all_blueprints(app):
    app.register_blueprint(login_page)
    app.register_blueprint(logout_page)
    app.register_blueprint(register_page)