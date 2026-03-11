from flask import Blueprint, redirect
from flask_login import login_required, logout_user, current_user

from database.classes import User
from database.db_session import create_session


logout_page = Blueprint('logout_page', __name__, template_folder='templates')
@login_required
@logout_page.route('/logout')
def logoutpage():
    logout_user()
    return redirect('/')