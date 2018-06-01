# -*- coding: utf-8 -*-
"""CIFAR10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iNHH57gdkcJmi8aGTACD_CP4XMPk_2vd
"""

from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

import numpy as np
import pandas as pd

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

from sklearn.model_selection import train_test_split
x_train , x_val , y_train , y_val = train_test_split( x_train , y_train , test_size = 0.15)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_val = x_val.astype('float32')

x_train = x_train / 255
x_test = x_test / 255
x_val = x_val / 255

image_rows = 32
image_colm = 32
num_classes = 10

# now making the CNN

#initialising the CNN
from keras.models import Sequential
classifier = Sequential()

#Adding the first convolution layer
from keras.layers import Conv2D
classifier.add( Conv2D ( 32, (3,3) , activation = 'relu' , input_shape = (image_rows , image_colm , 3)))
#adding the pooling layer
from keras.layers import MaxPooling2D
classifier.add( MaxPooling2D ( pool_size = (2,2) ))
#Flatteing
from keras.layers import Flatten
classifier.add( Flatten())

#now our CNN layer is ready , now feedinf it to an ANN
from keras.layers import Dense
classifier.add(Dense( output_dim = 64 , activation = 'relu'))
classifier.add(Dense( output_dim = 10 , activation = 'softmax'))

#now compiling our CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#now fitting our model
history = classifier.fit(x_train, y_train, batch_size=200, epochs= 50, verbose=1, validation_data=(x_val, y_val))

# analyzing the performance of our model
score = classifier.evaluate( x_test , y_test )

#making predictions
y_pred = classifier.predict( x_test)

# storing the results
y_pred_1 = np.argmax( y_pred , axis = 1)
y_test_1 = np.argmax( y_test , axis = 1)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix( y_test_1 , y_pred_1)

cm