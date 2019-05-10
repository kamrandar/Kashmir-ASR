# Load Packages
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from Train_data_generator import *
from Test_data_generator import *
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#np.set_printoptions(threshold=np.nan)
'''
with open('train_X.pkl') as f:
    Xtrain = f.read()
def train_gen(batchsz = 32):
    Xtrain = pickle.load('train_X.pkl')
    Ytrain = pickle.load('train_y.pkl')
    batchCount = 0
    while True:
        for line1,line2 in Xtrain,Ytrain:
            print(line1,line2)
            train_X = []
            train_Y = []
            train_X.append(line1)
            train_Y.append(line2)
            batchCount += 1
            if batchCount >= batchsz:
                batchCount = 0
                X_train = np.array(train_X)
                y_train = np.array(train_Y)
                yield X_train, y_train

def test_gen(batchsz = 32):
    Xtest = pickle.load('test_X.pkl')
    Ytest = pickle.load('test_y.pkl')
    batchCount = 0
    while True:
        for line1,line2 in Xtest,Ytest:
            print(line1,line2)
            test_X = []
            test_Y = []
            test_X.append(line1)
            test_Y.append(line2)
            batchCount += 1
            if batchCount >= batchsz:
                batchCount = 0
                X_test = np.array(test_X)
                y_test = np.array(test_Y)
                yield X_test, y_test

tgen = train_gen(batchsz=32)
vgen = test_gen(batchsz=32)
'''
verbose, no_of_epochs, batch_size = 1, 1, 64
n_timesteps, n_features, n_outputs = 3001, 13, 1000
inputshape=(n_timesteps,n_features)
model = Sequential()

model.add(LSTM(1000, input_shape=inputshape, return_sequences=False))
model.add(Dense(1000, kernel_initializer='normal', activation='linear'))
model.add(Dense(n_outputs, activation='softmax'))
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit_generator(Train_gen(),steps_per_epoch=656, epochs=no_of_epochs, verbose=verbose)
scores = model.evaluate(Test_gen(),step=18, verbose=1)
print('Accurracy: {}'.format(scores[1]))
#predict = model.predict(Xtrain)
print(model.summary())
