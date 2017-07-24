from PIL import Image, ImageFilter
import numpy as np
import random
import time

view = 2


def convert(im):

    # crop
    im = im.crop((230, 230, 794, 794))
   # im.save("output1.png")

    source = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixel = source[i, j]
            if pixel[0] != pixel[1] or pixel[1] != pixel[2] or pixel[2] != pixel[0]:
                # calculate the difference between them
                diff = max(pixel[0], pixel[1], pixel[2]) - min(pixel[0], pixel[1], pixel[2])

                # if the difference is small enough, the average will be set when the image is forced to grayscale
                if diff > 60:
                    source[i, j] = (255, 0, 0)

   # im.save("output2.png")

    interpolate(im, source)
   # im.save("output3.png")
    interpolate(im, source)
    interpolate(im, source)

    im = im.convert('LA')

    im = im.filter(ImageFilter.SMOOTH)
    im.thumbnail((166, 166), Image.ANTIALIAS)

    return im


def interpolate(im, source):
    # randomly iterate through
    coords = [(x, y) for x in range(im.size[0]) for y in range(im.size[1])]
    random.shuffle(coords)
    for i, j in coords:
        pixel = source[i, j]

        if pixel[0] == 255 or pixel[1] == 0 or pixel[2] == 0:
            set = []
            set.append(pixel)
            if i - view > 0:
                set.append(source[i - view, j])
                if j + view < im.size[0]:
                    set.append(source[i - view, j + view])
                if j - view > 0:
                    set.append(source[i - view, j - view])
            if i + view < im.size[1]:
                set.append(source[i + view, j])
                if j + view < im.size[0]:
                    set.append(source[i + view, j + view])
                if j - view > 0:
                    set.append(source[i + view, j - view])
            if j - view > 0:
                set.append(source[i, j - view])
            if j + view < im.size[0]:
                set.append(source[i, j + view])

            # remove all pixels that are red
            meanVals = []
            for pix in set:
               if pix[0] != 255 and pix[1] != 0 and pix[2] != 0:
                   meanVals.append(pix)

            if len(meanVals) > 0:
                # set to average
                newVal = tuple(map(np.mean, zip(*meanVals)))
                source[i, j] = (int(round(newVal[0])), int(round(newVal[1])), int(round(newVal[2])))


def isotherm(im, temp):
    #copy = [x[:] for x in source]
    source = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixel = source[i, j]
            if pixel[0] < temp:
                source[i, j] = (0, 0)

    im.save(str(temp) + ".png")
    #source = copy


if __name__ == '__main__':
    start = time.time()
    im = Image.open("input.jpg")
    im = convert(im)
    im.save("output.png")
#    pixels = np.asarray(im)[:, :, 0]
#    print(pixels)
#    print(pixels.shape)
#    pixels = pixels.flatten()
#    print(pixels)
#    print(pixels.shape)
#    pixels = pixels.reshape(166, 166)
#    print(pixels)
#    print(pixels.shape)
#    im = Image.fromarray(pixels)
#    im.save("out.png")
#    isotherm(im, 133)
    print("Took " + str(time.time() - start) + "s to complete.")