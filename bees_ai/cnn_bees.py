import os
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras import optimizers
import time
import pandas as pd

os.chdir('C:/Users/devg2/Desktop/data')

train_datagen = ImageDataGenerator(rescale = 1./255, 
                                   shear_range = 0.2, 
                                   zoom_range = 0.2,
                                   width_shift_range = 0.2,
                                   rotation_range = 90,
                                   height_shift_range = 0.2,
                                   horizontal_flip = True, 
                                   vertical_flip = True)

training_set = train_datagen.flow_from_directory('train',
                                                 target_size = (64, 64),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')
test_datagen = ImageDataGenerator(rescale = 1. / 255)

test_set = test_datagen.flow_from_directory('test',
                                                 target_size = (64, 64),
                                                 batch_size = 16)

'''val_datagen = ImageDataGenerator(rescale = 1./255)
val_set = test_datagen.flow_from_directory('val',
                                            target_size = (64, 64),
                                            batch_size = 16,
                                            class_mode = 'categorical')'''

classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation='relu'))
# Convo 1
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
'''# Convo 2
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))'''

classifier.add(Dropout(0.25))
'''# Convo 3
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Convo 4
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Convo 5
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))'''
# Flatten
classifier.add(Flatten())
# Full connection
classifier.add(Dense(128, activation='relu'))
classifier.add(Dropout(0.5))

'''classifier.add(Dense(256, activation='relu'))
classifier.add(Dropout(0.5))'''
# Output layer
classifier.add(Dense(2, activation = 'softmax'))

classifier.compile(loss = 'categorical_crossentropy', optimizer = 'rmsprop', metrics = ['accuracy'])

# Definir callbacks

start_time = time.time()
history = classifier.fit_generator(training_set,
                         steps_per_epoch = 3969/16,
                         epochs = 10#,
                         #validation_data = val_set,
                         #validation_steps = 992/16,
                         #workers = 8,
                         #max_q_size = 100
                         )
print('Learning took {0} minutes.'.format((time.time() - start_time)/60))

classifier.summary()

classifier.save('bees_model.h5')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc = 'upper left')
plt.show()

# Plot history
#print(history.history.keys())
print('val_acc: ',min(history.history['val_acc']))
print('val_loss: ',min(history.history['val_loss']))
print('acc: ',min(history.history['acc']))
print('loss: ',min(history.history['loss']))

training_set.class_indices

prob = classifier.predict_generator(test_set) #predict_proba / predict_generator

counter = os.listdir('C:/Users/devg2/Desktop/for_model/model/data/test/test')
counter = counter[:-1]
solution = pd.DataFrame({"id": counter, "label":list(prob)})
solution['id'] = solution['id'].replace('.jpg', ' ', regex=True)
solution['honey_bee'], solution['bumble_bee'] = zip(*solution['label'])
solution = solution.drop(['label'], axis = 1)

solution.to_csv("bees_submission.csv", index = False)