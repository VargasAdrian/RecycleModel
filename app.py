#guide https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/

import numpy
from tensorflow import keras
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.datasets import cifar10
from keras import Sequential

seed = 21

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0

# One-hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
class_num = y_test.shape[1]

model = Sequential()
model.add(keras.layers.layer1)
model.add(keras.layers.layer2)
model.add(keras.layers.layer3)
