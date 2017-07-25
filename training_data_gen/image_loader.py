import io
from PIL import Image
from urllib import request
from image_converter import convert
from validation import validate_edges
from common import wind_to_dvorak
import main


def load_image(image):
    fd = request.urlopen(image.global_url + image.url)
    image_file = io.BytesIO(fd.read())
    im = Image.open(image_file)

    # convert
    im = convert(im)

    if validate_edges(im):
        # throw out image
        return False

    # save
    if main.save_images:
        im.save("./images/" + image.to_string() + ".png")

    # get dvorak rating
    dvorak = wind_to_dvorak(image.wind)

    return [im, dvorak]
