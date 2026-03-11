from flask import Blueprint, render_template
from database.classes import Modules, Points
from functions.map_functions import stations_with_radiuses

image_map = Blueprint('image_map', __name__, template_folder='templates')
@image_map.route('/image/map/<img_url>')
def image_map_page(img_url):
    context = {
        'img_path': stations_with_radiuses(img_url),
    }
    return render_template('main.html', **context)