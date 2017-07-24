from urllib import request
from html_parser import StormPage
import validation
import numpy as np
import io
from PIL import Image
from image_converter import convert


def load_storm(url):
    res = request.urlopen(url)
    output = res.read().decode("utf-8")

    # parse
    parser = StormPage()
    parser.feed(output)

    intensity_ptr = 0
    images = np.asarray(parser.images)
    for i in range(len(images)):
        image = images[i]
        # intensity increase to deal with
        if image.wind > intensity_ptr:
            if intensity_ptr == 0 and image.wind <= 30:
                intensity_ptr = image.wind
            elif intensity_ptr == 0:
                # storms intensity started too high, keep trying for a more realistic beginning if possible
                continue
            else:
                # check the incoming sequence and this image if its valid
                if not validation.validateSequence(image, np.flipud(images[:i])):
                    # not valid, keep going
                    continue
                else:
                    # up the intensity ptr
                    intensity_ptr = image.wind

            # all good, download the image now
            fd = request.urlopen(url + image.url)
            image_file = io.BytesIO(fd.read())
            im = Image.open(image_file)

            # convert
            im = convert(im)

            # save
            im.save("./images/" + image.date + image.ztime + " "  + image.name + " " + str(image.wind) + "kts.png")
        if image.wind < intensity_ptr:
            intensity_ptr = image.wind


if __name__ == '__main__':
    load_storm("https://www.nrlmry.navy.mil/tcdat/tc16/ATL/14L.MATTHEW/ir/geo/1km_bw/")