from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wavfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import librosa
import pickle

temp2 = []
for i in range(1, 5):
    y, sr = librosa.load('kamran_sopore\\' + str(i) + '.wav')
    audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
    print(str(i))

    mfcc_features = mfcc(audio)

    print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
    print('Length of each feature =', mfcc_features.shape[1])

    temp2.append([str(i), [mfcc_features]])

with open('test_Samples.obj', 'wb') as f:
 pickle.dump(temp2, f)
for x in temp2:
 print('-----------------------------------------------------------------')
 print(x)
 print('-----------------------------------------------------------------')

with open('test_Samples.obj', 'rb') as f:
    object_file = pickle.load(f)
    # converting lists to pandas dataframe_buffer
    df = pd.DataFrame(object_file, columns=['label', 'data'])
    x_data = df['data']
    y2_label=df['label']
    X2=[]
    for x in x_data:
        X2.append(x[0])

X2 = np.array(X2)
X2 = pad_sequences(X2)
print(X2.shape)
y2_label = to_categorical(y2_label)
print(y2_label.shape)
