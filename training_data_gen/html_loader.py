from urllib import request
from html_parser import StormPage, BasinPage
import validation
import numpy as np
from image_loader import load_image
import concurrent.futures
import time
import main
import to_hdf5


def load_storm(url):
    res = request.urlopen(url)
    output = res.read().decode("utf-8")

    # parse
    parser = StormPage()
    parser.feed(output)

    # process incoming data
    intensity_ptr = 0
    images = np.asarray(parser.images)
    to_dl = []
    for i in range(len(images)):
        image = images[i]
        # intensity increase to deal with
        if image.wind > intensity_ptr:
            if intensity_ptr == 0 and image.wind <= 30 and validation.validate(image):
                intensity_ptr = image.wind
            elif intensity_ptr == 0:
                # storms intensity started too high, keep trying for a more realistic beginning if possible
                continue
            else:
                # check the incoming sequence and this image if its valid
                if not validation.validate_sequence(image, np.flipud(images[:i])):
                    # not valid, keep going
                    continue
                else:
                    # up the intensity ptr
                    intensity_ptr = image.wind

            # all good, mark the image to download
            image.global_url = url
            to_dl.append(image)
        if image.wind < intensity_ptr:
            intensity_ptr = image.wind

    # download and process the images
    executor = concurrent.futures.ProcessPoolExecutor(None)
    images = list(executor.map(load_image, to_dl))
    to_hdf5.save(images)


def load_basin(url):
    res = request.urlopen(url)
    output = res.read().decode("utf-8")

    # parse
    parser = BasinPage()
    parser.feed(output)

    # process incoming data, skip invests
    to_dl = []
    for stormURL in parser.urls:
        if stormURL[0] == "9":
            continue
        newURL = url + stormURL + "ir/geo/1km_bw/"
        to_dl.append(newURL)

    # download storms
    for url in to_dl:
        load_storm(url)


def load_year(url):
    for basin in main.basins:
        load_basin(url + basin)


if __name__ == '__main__':
    start = time.time()
    load_storm("https://www.nrlmry.navy.mil/tcdat/tc16/ATL/16L.OTTO/ir/geo/1km_bw/")
    print("Took " + str(time.time() - start) + "s to complete.")