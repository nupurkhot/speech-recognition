import sys
from matplotlib import pyplot
import keras

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense,Dropout
from keras.layers import Flatten,BatchNormalization
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
'''
def summarize_plots(history):
	# plot loss
	pyplot.subplot(211)
	pyplot.title('Cross Entropy Loss')
	pyplot.plot(history.history['loss'], color='blue', label='Train')
	pyplot.plot(history.history['val_loss'], color='red', label='test')
	pyplot.show()
	# plot accuracy
	pyplot.subplot(212)
	pyplot.title('Classification Accuracy')
	pyplot.plot(history.history['acc'], color='blue', label='train')
	pyplot.plot(history.history['val_acc'], color='red', label='test')
	pyplot.show()
	# save plot to file

	filename = sys.argv[0].split('/')[-1]
	pyplot.savefig(filename + '_plot.png')
	pyplot.close()
'''

def define_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(64, 64 ,3)))
	model.add(BatchNormalization())

	model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
	model.add(BatchNormalization())

	model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(BatchNormalization())
	model.add(Dropout(0.25))
	model.add(Dense(64, activation='relu'))
	model.add(BatchNormalization())
	model.add(Dropout(0.4))
	model.add(Dense(10, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
	return model

model=define_model()

train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0, zoom_range=0, horizontal_flip=False, width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width), 
height_shift_range=0.1)  # randomly shift images vertically (fraction of total height))

test_datagen = ImageDataGenerator(rescale=1./255)  

train_generator = train_datagen.flow_from_directory('/home/speech-recognition/data/train-spectrograms',target_size=(64, 64), batch_size=50, shuffle=True)
validation_generator = test_datagen.flow_from_directory('/home/speech-recognition/data/test-spectrograms',target_size=(64, 64),batch_size=50, shuffle=True)
#print validation_generator


history = model.fit_generator(train_generator,steps_per_epoch=36,verbose=1, validation_data=validation_generator,validation_steps=4,epochs=100)
#print(model.summary())

# list all data in history
print(history.history.keys())

import matplotlib.pyplot as plt
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

# prediction on validation data
test_image = image.load_img('/home/speech-recognition/data/test-spectrograms/1/1_jackson_0.png')
test_image = image.img_to_array(test_image)
result=model.predict(test_image)
print(result)