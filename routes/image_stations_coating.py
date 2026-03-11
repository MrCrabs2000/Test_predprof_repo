from flask import Blueprint, render_template
from database.classes import Modules, Points


image_stations_coating = Blueprint('image_stations_coating', __name__, template_folder='templates')
@image_stations_coating.route('/image/stations/coating/<>')
def image_stations_coating_page():
