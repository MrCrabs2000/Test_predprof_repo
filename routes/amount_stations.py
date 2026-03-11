from flask import Blueprint, render_template
from database.classes import Modules, Points


amount_stations = Blueprint('amount_stations', __name__, template_folder='templates')
@amount_stations.route('/amount/stations/<>')
def amount_stations_page():
