# Load Packages
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import LSTM
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
import os
import librosa
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#np.set_printoptions(threshold=np.nan)

X = []
with open('Features_Dataset_trimmed_mfcc_1001_Samples.obj', 'rb') as f:
    object_file = pickle.load(f)
    # converting lists to pandas data frame buffer
    df = pd.DataFrame(object_file, columns=['label', 'data'])
    x_data = df['data']
    y_label = df['label']
    X = []
    for x in x_data:
        X.append(x[0])

X = np.array(X)
X = pad_sequences(X)
y_label = np.array(y_label)
y_label = to_categorical(y_label)
print(X.shape)
print(y_label.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y_label, test_size=0.2, shuffle=True)


with open('Train_X.pkl', 'wb') as f1:
    pickle.dump(X_train, f1)

with open('Train_y.pkl', 'wb') as f2:
    pickle.dump(y_train, f2)

with open('Test_X.pkl', 'wb') as f3:
    pickle.dump(X_test, f3)

with open("test_y.pkl", 'wb') as f4:
   pickle.dump(y_test, f4)
'''
def train_gen(batchsz = 32):
    f1 = open('train_X.pkl','rb')
    Xtrain = pickle.load(f1)
    f2 = open('train_y.pkl', 'rb')
    Ytrain = pickle.load(f2)
    batchCount = 0
    train_X = []
    train_Y = []
    i = 0
    while True:
        for line1 in Xtrain:
            train_Y.append(Ytrain[i])
            train_X.append(line1)
            batchCount += 1
            i = i+1
            if batchCount >= batchsz:
                batchCount = 0
                X = np.array(train_X)
                Y = np.array(train_Y)
                yield (X, Y)
                train_X = []
                train_Y = []
        i=0

def test_gen(batchsz = 32):
    f1 = open('Test_X.pkl', 'rb')
    Xtest = pickle.load(f1)
    f2 = open('test_y.pkl', 'rb')
    Ytest = pickle.load(f2)
    batchCount = 0
    test_X = []
    test_Y = []
    i = 0
    while True:
        for line1 in Xtest:
            test_Y.append(Ytest[i])
            test_X.append(line1)
            batchCount += 1
            i = i+1
            if batchCount >= batchsz:
                batchCount = 0
                X = np.array(test_X)
                Y = np.array(test_Y)
                yield (X, Y)
                test_X = []
                test_Y = []
        i=0
#temp1 = train_gen()
#temp2 = next(temp1)
#print(temp2[1])

#temp3 = test_gen()
#temp4 = next(temp3)
#print(temp4[1])
'''
