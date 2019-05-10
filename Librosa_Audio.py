import librosa
import matplotlib.pyplot as plt
import wave
import os
import pickle
import numpy as np
#np.set_printoptions(threshold=np.nan)
temp = []
for i in range(1, 251):
        # Load some audio
        y, sr = librosa.load('Female_south\\' + str(i) + '.wav')
        # Trim the beginning and ending silence
        yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        #print(librosa.get_duration(y), librosa.get_duration(yt))
        temp.append([str(i), [yt]])
for i in range(1, 900):
        # Load some audio
        y, sr = librosa.load('Male_center\\' + str(i) + '.wav')
        # Trim the beginning and ending silence
        yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        #print(librosa.get_duration(y), librosa.get_duration(yt))
        temp.append([str(i), [yt]])
for i in range(1,3107):
        # Load some audio
        try:
            y, sr = librosa.load('Male_South\\' + str(i) + '.wav')
        except EOFError:
            print("Error: EOF or empty input!")
            continue
        # Trim the beginning and ending silence
        yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        #print(librosa.get_duration(y), librosa.get_duration(yt))
        temp.append([str(i),[yt]])

for i in range(1,1000):
        # Load some audio
        try:
            y, sr = librosa.load('Male_North\\' + str(i) + '.wav')
        except EOFError:
            print("Error: EOF or empty input!")
            continue
        # Trim the beginning and ending silence
        yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        #print(librosa.get_duration(y), librosa.get_duration(yt))
        temp.append([str(i),[yt]])
for i in range(1,650):
        # Load some audio
        try:
            y, sr = librosa.load('Female_center\\' + str(i) + '.wav')
        except EOFError:
            print("Error: EOF or empty input!")
            continue
        # Trim the beginning and ending silence
        yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        #print(librosa.get_duration(y), librosa.get_duration(yt))
        temp.append([str(i), [yt]])
with open('Features_Dataset_trimmed_original.obj', 'wb') as f:
        pickle.dump(temp, f)
for x in temp:
        print('-----------------------------------------------------------------')
        print(x)
        print('-----------------------------------------------------------------')



 