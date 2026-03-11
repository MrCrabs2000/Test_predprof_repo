from .image_map import image_map
from .image_modules import image_modules
from .image_stations import image_stations
from .image_stations_coating import image_stations_coating
from .amount_stations import amount_stations


def register_all_blueprints(app):
    app.register_blueprint(image_map)
    app.register_blueprint(image_modules)
    app.register_blueprint(image_stations)
    app.register_blueprint(image_stations_coating)
    app.register_blueprint(amount_stations)