import h5py
from PIL import Image
import numpy as np
import main


def save(images):
    f = h5py.File("../training_data/" + main.data_out_file_name + ".hdf5", "a")
    try:
        x_set = f["."]["x_set"]
    except KeyError:
        x_set = f.create_dataset("x_set", (1, 166, 166), maxshape=(None, 166, 166), dtype='u1')

    try:
        y_set = f["."]["y_set"]
    except KeyError:
        y_set = f.create_dataset("y_set", (1, 16), maxshape=(None, 16), dtype='u1')

    for im in images:
        if im is False:
            continue

        # set image
        pixels = np.asarray(im[0])[:, :, 0]
        x_set[x_set.shape[0] - 1, :, :] = pixels
        x_set.resize(x_set.shape[0] + 1, 0)

        # set label
        y_set[y_set.shape[0] - 1, :] = im[1]
        y_set.resize(y_set.shape[0] + 1, 0)

"""
f = h5py.File('test.hdf5', 'a')
dset = f["."]["x_set"]

pixels = dset[0,:,:]

im = Image.fromarray(pixels)
im.save("out0.png")"""
