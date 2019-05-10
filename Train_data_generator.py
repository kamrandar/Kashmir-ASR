import os
import librosa
from python_speech_features import mfcc
import numpy as np
from keras.preprocessing.sequence import pad_sequences


# Training Generator
def Train_gen(batchsz=64):
    while True:
        PATH = 'Audio Synthesis\\'

        batchcount = 0
        Xtrain = []
        Ytrain = []

        for root, dirs, files in os.walk(PATH):

            for name in files:
                label, _, _ = name.partition('.')
                # print('--Processing--' + name)

                y, sr = librosa.load(root + '\\' + name)
                audio, _ = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)

                mfcc_features = mfcc(audio)
                Xtrain.append(mfcc_features)

                a = np.zeros(1000)
                arr = np.zeros_like(a, dtype=int)
                arr[int(label) - 1] = 1

                Ytrain.append(arr)
                Y_train = np.array(Ytrain)
                X_train = pad_sequences(Xtrain, 3001)
                #X_train = X_train.reshape(X_train.shape[1],X_train.shape[2], 1)
                batchcount += 1
                if batchcount >= batchsz:
                    yield (X_train, Y_train)
                    batchcount = 0
                    Xtrain = []
                    Ytrain = []


# temp = Train_gen()
'''
print("-----------------------")
print(next(temp))
print("-----------------------")
print(next(temp))
'''
