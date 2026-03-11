from PIL import Image
from pathlib import Path
from database.db_session import create_session
from database.classes import Points


def stations_with_radiuses(filename):
    dirr = Path(__file__).parent.parent
    last_dirr = dirr / 'static' / 'images'
    last_dirr.mkdir(parents=True, exist_ok=True)
    path = last_dirr / filename

    try:
        Image.open(path)
        session = create_session()
        points = session.query(Points).all()
    




