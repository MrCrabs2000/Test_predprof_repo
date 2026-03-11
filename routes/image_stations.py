from flask import Blueprint, render_template
from database.classes import Modules, Points


image_stations = Blueprint('image_modules', __name__, template_folder='templates')
@image_stations.route('/image/stations/<>')
def image_stations_page():
