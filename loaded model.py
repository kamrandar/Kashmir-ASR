from keras.models import load_model
import numpy as np
from keras.preprocessing.sequence import pad_sequences
import librosa
from keras.models import  model_from_json
import sqlite3
import os
import pickle
import pandas as pd
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
np.set_printoptions(threshold=np.nan)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
with open('kamran.obj', 'rb') as f:
    object_file = pickle.load(f)

    # converting lists to pandas data frame buffer
    df = pd.DataFrame(object_file, columns=['label', 'data'])
    x_data = df['data']
    y_label = df['label']
    #print(df)
    X = []
    for x in x_data:
        X.append(x[0])

X = np.array(X)
X = pad_sequences(X, 3001)
y_label = np.array(y_label)
y_label = to_categorical(y_label)

print(X.shape)
print(y_label.shape)

X_data = X.reshape(X.shape[0],X.shape[1],X.shape[2],1)

print(X_data.shape)


# load json and create model

json_file = open('relu_15_sgd.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model =  model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("relu_15_sgd.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
#loaded_model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
#score = loaded_model.evaluate(X_data, y_label, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

# make a prediction
ynew = loaded_model.predict(X_data[:10])
# show the inputs and predicted outputs
#print(ynew)
result = []
for data in ynew:
   result.append(np.argmax(data))

#print(result,len(result))
conn = sqlite3.connect('kashmir_TEXT_DB')
c = conn.cursor()
c.execute("SELECT Text,s_no FROM Ktext_TABLE WHERE s_no<= 20")
original = c.fetchall()
for words in original:
    print(words, end='')

print('\n')
for i in range(len(result)):
    conn = sqlite3.connect('kashmir_TEXT_DB')
    c = conn.cursor()
    c.execute("SELECT Text,s_no FROM Ktext_TABLE WHERE rowid IN {}".format(str(tuple(result))))
    table = c.fetchall()

for data in table:
        print(data, end='')

#for data2 in y_label[:20]:
#    print(np.argmax(data2))

