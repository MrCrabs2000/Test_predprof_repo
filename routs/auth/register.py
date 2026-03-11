from flask import Blueprint, request, render_template, redirect
from werkzeug.security import generate_password_hash
from flask_login import login_user

from database.db_session import create_session
from database.classes import User


register_page = Blueprint('register_page', __name__, template_folder='templates')
@register_page.route('/register', methods=['GET', 'POST'])
def registerpage():
    if request.method == 'GET':
        return render_template('auth/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    second_password = request.form.get('second_password')

    if not all([login, password, second_password]):
        return redirect('/')
    
    session = create_session()

    user = session.query(User).filter_by(login=login).first()

    if user or password != second_password or len(password) < 6:
        return redirect('/')
    
    new_user = User(login=login, password=generate_password_hash(password))
    
    try:
        session.add(new_user)
        session.commit()
        login_user(new_user)
    except Exception as e:
        print(e)
    finally:
        session.close()
        return redirect('/')