from flask import Blueprint, render_template
from database.classes import Modules, Points


image_map = Blueprint('image_map', __name__, template_folder='templates')
@image_map.route('/image/map/<img_url>')
def image_map_page(img_url):
    contex = {
        'img_path': 
    }