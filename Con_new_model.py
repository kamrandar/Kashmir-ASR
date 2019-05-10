from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
from Train_data_generator import *
from Test_data_generator import *
np.set_printoptions(threshold=np.nan)

Xtrain, Ytrain = next(Train_gen())
Xtest, Ytest = next(Test_gen())

verbose, no_of_epochs, batch_size = 1, 10, 32
n_timesteps, n_features, n_outputs = 3001, 13, 1000


model = Sequential()
model.add(Conv1D(filters=50, kernel_size=3, strides=3, activation='relu',input_shape=(n_timesteps,n_features)))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=50, kernel_size=3, strides=3, activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Conv1D(filters=50, kernel_size=3, strides=3, activation='relu'))
model.add(MaxPooling1D(pool_size=2))

model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(1000))
model.add(Dropout(0.5))
model.add(Dense(n_outputs, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit network
model.fit_generator(Train_gen(), steps_per_epoch=1312, epochs=no_of_epochs, verbose=verbose)

# evaluate model
_, accuracy = model.evaluate_generator(Test_gen(), steps=18, verbose=0)
print("Accuracy: %.2f%%" % (accuracy[1]*100))


#Predict Model
predict = model.predict(Xtest)
print(predict)

model.save('kashmiri_speech_Model.json')

print(model.summary())

