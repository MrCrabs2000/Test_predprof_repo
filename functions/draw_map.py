from PIL import Image, ImageDraw
from api.api import api_get


def draw_grid(drawer, grid_size=64, line_color=(0, 0, 0), line_width=1, size=(256, 256)):
    width, height = size[0], size[1]
    for x in range(0, width, grid_size):
        drawer.line([(x, 0), (x, height)], fill=line_color, width=line_width)
    for y in range(0, height, grid_size):
        drawer.line([(0, y), (width, y)], fill=line_color, width=line_width)


def draw_circle(drawer, x, y, r, height=256):
    drawer.ellipse((x - r, height - y - r, x + r, height - y + r), fill="blue", outline="black")


def draw_map_with_modules():
    modules_info = api_get("https://olimp.miet.ru/ppo_it/api/coords")
    coords_listener = modules_info["message"]["listener"]
    coords_sender = modules_info["message"]["sender"]

    r_listener = 32
    r_sender = 32

    img = Image.new("RGB", (256, 256), "white")
    draw = ImageDraw.Draw(img)

    draw_grid(draw)

    draw_circle(draw, coords_listener[0], coords_listener[1], r_listener)
    draw_circle(draw, coords_sender[0], coords_sender[1], r_sender)

    img.show()
    # img.save("circle.png")


draw_map_with_modules()
