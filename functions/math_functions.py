from math import sqrt
from typing import Optional


def check_relation(coords: list[int] = None, type='listener'):
    x, y, z = coords[:3]
    rx, ry, rz = coords[3:]
    if type == 'listener':
        radius = 32
    else:
        radius = 64

    rast = sqrt(((x - rx) ** 2) + ((y - ry) ** 2) + ((z - rz) ** 2))

    if rast <= radius:
        return True
    else:
        return False


def higher_points(highers: list[list[int]] = None):
    mx = 0
    highers_ls = []
    for points in highers:
        if max(points) > mx:
            mx = max(points)

    for points in highers:
        for point in points:
            if point == mx:
                highers_ls.append(point)

    return highers_ls



