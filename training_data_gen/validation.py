import main


def validate(img):
    # unknown satellite, could be garbage
    if img.satellite not in main.valid_satellites:
        return False

    # satellite didn't hit 98% of the storm
    if img.pc < 98:
        return False

    return True


def validate_sequence(img, prevImgs):
    if not validate(img):
        return False


    # check if there was another intensity change in the last 3 hours
    for i in prevImgs:
        if i.wind != img.wind:
            if ((img.time - i.time).seconds / 3600) <= 3:
                return False

        if ((img.time - i.time).seconds / 3600) > 3:
            return True

    return True


# due to issues with satellite imagery, sometimes the edges will contain no data (black pixels) despite saying the photo is valid
# here we check the average intensity of all edges
# if any edge is below 75 average, then there's a bunch of pure black pixels


def validate_edges(im):
    source = im.load()

    sum1 = 0
    ctr = 0

    # sample the left edge
    for i in range(0, 20, 2):
        for j in range(0, im.size[1], 2):
            pixel = source[i, j]
            sum1 += pixel[0]
            ctr += 1

    average1 = sum1 / ctr

    sum2 = 0
    ctr = 0

    # sample the right edge
    for i in range(im.size[0] - 20, im.size[0], 2):
        for j in range(0, im.size[1], 2):
            pixel = source[i, j]
            sum2 += pixel[0]
            ctr += 1

    average2 = sum2 / ctr

    sum3 = 0
    ctr = 0

    # sample the top edge
    for i in range(0, im.size[1], 2):
        for j in range(0, 20, 2):
            pixel = source[i, j]
            sum3 += pixel[0]
            ctr += 1

    average3 = sum3 / ctr

    sum4 = 0
    ctr = 0

    # sample the bottom edge
    for i in range(0, im.size[1], 2):
        for j in range(im.size[0] - 20, im.size[0], 2):
            pixel = source[i, j]
            sum4 += pixel[0]
            ctr += 1

    average4 = sum4 / ctr

    lowestAvg = min(average1, average2, average3, average4)
    return lowestAvg < 75