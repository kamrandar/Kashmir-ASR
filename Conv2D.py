from keras.models import Sequential
from keras import *
from keras.layers import Dense, Dropout, Flatten,Conv2D, MaxPooling2D
from Train_data_generator import *
from Test_data_generator import *
np.set_printoptions(threshold=np.nan)
TF_CPP_MIN_LOG_LEVEL = 2

verbose, no_of_epochs, batch_size = 1, 4, 32
n_timesteps, n_features, n_outputs = 3001, 13, 1000

inputshape=(n_timesteps,n_features,1)

Xtrain, Ytrain = next(Train_gen())
Xtest, Ytest = next(Test_gen())

Xtrain = Xtrain.reshape(Xtrain.shape[0],Xtrain.shape[1],Xtrain.shape[2],1)

print(Xtrain.shape)

inputshape=(n_timesteps,n_features,1)

# The first layer with 32 filters of window size 3x3 and Second with 32 filters W(3x3)
model = Sequential()

model.add(Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=inputshape))
model.add(MaxPooling2D(pool_size=3))
model.add(Dropout(0.3))

model.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
model.add(MaxPooling2D(pool_size=3))
model.add(Dropout(0.3))

model.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
model.add(MaxPooling2D(pool_size=3))
model.add(Dropout(0.3))

model.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
model.add(MaxPooling2D(pool_size=3))
model.add(Dropout(0.3))

model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1000, activation='relu'))
model.add(Flatten())
model.add(Dense(n_outputs, activation='softmax'))

# Dense Layers
model.add(Flatten())
#model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1000, activation='relu'))

# Output Layer
model.add(Dense(n_outputs, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit model
model.fit(Xtrain,Ytrain, epochs=no_of_epochs,steps_per_epoch=1312,verbose=1)

# Evaluate model
scores = model.evaluate(Xtest,Ytest, steps=18, verbose=1)
print("Accuracy: %.2f%%" % (scores[1]*100))

#Predict Model
predict = model.predict(Xtest)
print(predict)

# Save Model As .Json
model.save('kashmiri_speech_Model.json')

# Display model Summary
print(model.summary())
