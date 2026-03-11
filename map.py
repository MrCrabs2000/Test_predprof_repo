from PIL import Image, ImageDraw
from pathlib import Path
from database import db_session
from database.classes import Points


def stations_with_radiuses(filename):

    dirr = Path(__file__).parent.parent
    last_dirr = dirr / 'static' / 'images'
    last_dirr.mkdir(parents=True, exist_ok=True)
    path = last_dirr / filename
    try:
        image = Image.open(f'static/images/{filename}')
    except Exception as e:
        print('Файла нет')
        image = Image.new('RGB', (256, 256), (255, 255, 255))
    finally:
        try:
            db_session.init_database()
            session = db_session.create_session()
            points = session.query(Points).all()

            draw = ImageDraw.Draw(image)

            for point in points:
                x, y = point.coord_x, point.coord_y
                if point.status:
                    if point.point_module == 'listener' and len(points.point_module) != 0:
                        r = 32
                        draw.ellipse((x - r, y - r, x + r, y + r), fill='red', outline=(0, 0, 0))
                    else:
                        r = 64
                        draw.ellipse((x - r, y - r, x + r, y + r), fill='blue', outline=(0, 0, 0))

            width, height = 256, 256
            for x in range(0, width, 64):
                draw.line([(x, 0), (x, height)], fill=(0, 0, 0), width=1)
            for y in range(0, height, 64):
                draw.line([(0, y), (width, y)], fill=(0, 0, 0), width=1)

            image.save('static/images/draw.png')
            session.close()
        except Exception as e:
            print(f'Ошибочка: {e}')
        finally:
            return f'static/images/{filename}'

stations_with_radiuses('draw.png')