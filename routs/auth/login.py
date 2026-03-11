from flask import Blueprint, request, render_template, redirect
from werkzeug.security import check_password_hash
from flask_login import login_user

from database.db_session import create_session
from database.classes import User


login_page = Blueprint('login_page', __name__, template_folder='templates')
@login_page.route('/login', methods=['GET', 'POST'])
def loginpage():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not all([login, password]):
        return redirect('/')
    
    session = create_session()

    user = session.query(User).filter_by(login=login).first()

    if not user or not check_password_hash(user.password, password):
        return redirect('/')
    
    try:
        login_user(user)
    except Exception as e:
        print(e)
    finally:
        session.close()
        return redirect('/')