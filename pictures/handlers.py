from datetime import datetime as dt

from PIL import Image
from requests import get


def get_image(link):
    content = get(link).content
    date = dt.now()
    filename = f'{date}.jpg'
    with open(f'media/images/{filename}', mode='wb') as file:
        file.write(content)
    return f'images/{filename}'


def get_image_size(path):
    image = Image.open(path)
    return image.size


def check_proportions(old_width, old_height, width, height):
    return old_width // width == old_height // height


def resize_image(image_path, new_width, new_height):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_image.save(f'media/{image_path}')
