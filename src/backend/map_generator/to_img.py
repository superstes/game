import numpy as np
from PIL import Image

from config import export_file, CHUNK_SIZE

COLOR_DEEPWATER = (0, 62, 178)
COLOR_WATER = (9, 82, 198)
COLOR_SAND = (254, 224, 179)
COLOR_GRASS = (9, 120, 93)
COLOR_DARKGRASS = (10, 107, 72)
COLOR_DARKESTGRASS = (11, 94, 51)
COLOR_DARKROCKS = (140, 142, 123)
COLOR_ROCKS = (160, 162, 143)
COLOR_BLACKROCKS = (53, 54, 68)
COLOR_SNOW = (255, 255, 255)


def _get_color(height: float, max_height: float):
    factor = 255 / max_height
    h = height * factor

    if h < 0:
        h = 0

    if h > 255:
        h = 255

    if h <= 1:
        return COLOR_DEEPWATER
    if h <= 1.5:
        return COLOR_WATER
    if h <= 2:
        return COLOR_SAND
    if h <= 18:
        return COLOR_GRASS
    if h <= 30:
        return COLOR_DARKGRASS
    if h <= 70:
        return COLOR_DARKESTGRASS
    if h <= 115:
        return COLOR_DARKROCKS
    if h <= 125:
        return COLOR_ROCKS
    if h <= 220:
        return COLOR_BLACKROCKS

    return COLOR_SNOW


def create_map_img(map_data: list[float], pos_x: int, pos_y: int, max_height: float):
    colour_map = np.zeros((CHUNK_SIZE, CHUNK_SIZE, 3), dtype=np.uint8)

    for i in range(CHUNK_SIZE * CHUNK_SIZE):
        xi, yi, zi = i * 3, i * 3 + 1, i * 3 + 2
        xr, yr = map_data[xi] - pos_x, map_data[yi] - pos_y
        colour_map[xr, yr] = _get_color(map_data[zi], max_height)

    image = Image.fromarray(colour_map, 'RGB')
    image.save(f"{export_file(pos_x, pos_y)}.png")
    return image
