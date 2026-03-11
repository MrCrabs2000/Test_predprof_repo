from flask import Blueprint, render_template
from database.classes import Modules, Points


image_modules = Blueprint('image_modules', __name__, template_folder='templates')
@image_modules.route('/image/modules/<>')
def image_modules_page():
