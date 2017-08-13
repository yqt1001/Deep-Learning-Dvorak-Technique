from keras.utils.io_utils import HDF5Matrix
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation, Convolution2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
from PIL import Image
import numpy as np
import main


def add_dim(data):
    return data[:, :, 0]
"""
# load in the data
path = "../training_data/" + main.training_in_file_name + ".hdf5"
cutoff = int(main.training_set_size * .85)  # use 85% of data for training, 15% for testing
X_train = HDF5Matrix(path, "x_set", start=0, end=cutoff)
Y_train = HDF5Matrix(path, "y_set", start=0, end=cutoff)

X_test = HDF5Matrix(path, "x_set", start=cutoff, end=main.training_set_size)
Y_test = HDF5Matrix(path, "y_set", start=cutoff, end=main.training_set_size)

# change this later, use this base to start messing around
model = Sequential()
BatchNormalization(input_shape=(166, 166, 1))
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(166, 166, 1)))
model.add(Activation('relu'))
BatchNormalization(axis=1)
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

BatchNormalization()
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(16, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

hist = model.fit(X_train, Y_train, batch_size=32, epochs=5, verbose=1, shuffle="batch")
print(hist.history)

model.evaluate(X_test, Y_test, batch_size=32)
model.save("test.hdf5")"""

source = np.zeros((1, 166, 166, 1))
im = Image.open("test.png")
pixels = np.asarray(im)[:, :, 0]
source[0, :, :, :] = pixels[..., None]

model = load_model('test.hdf5')

prediction = model.predict(source)
print(prediction)
