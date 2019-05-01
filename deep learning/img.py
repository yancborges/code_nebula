import keras
import numpy as np 
from parser import load_data

path = 'C:/Users/Yan/Desktop/Scripting/data_sets/dogs-vs-cats/'

train = load_data(path + 'train')
test = load_data(path + 'test')

model = Sequential()
model.add(Convolution2D(32,3,3, input_shape=(img_width, img_height,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(32,3,3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(64,3,3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.fit_generator(train,samples_per_epoch=2048,nb_epoch=30,validation_data=test,nb_val_samples=832)
model.save_weights('models/simples_CNN.h5')

img = image.load_img('test/1.jpg', target_size=(224,224))
pred = model.predict(img)
print(pred)







