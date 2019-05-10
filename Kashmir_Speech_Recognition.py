from tkinter import *
from tkinter import ttk
import tkinter as tk
from keras.preprocessing.sequence import pad_sequences
from pygame import mixer
from tkinter import messagebox
from keras.models import  model_from_json
import os
import sqlite3
import pandas as pd
from python_speech_features import mfcc
import librosa
from pyaudio import *
import speech_recognition as sr
import numpy as np
import pickle
f1=('ariel',18,'bold')
root = Tk()
w=1000
h=300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Kashmiri Audio Data Set Recorder")
root.iconbitmap('mic.ico')

emo = tk.StringVar(root)

photo = PhotoImage(file='microphone.png').subsample(20, 20)

def listen():
    global audio
    if os.path.isfile('microphone-results.wav'):
        os.remove('microphone-results.wav')
    else:
        r = sr.Recognizer()
        r.pause_threshold = 0.6
        r.energy_threshold = 500
        m = sr.Microphone()
        with m as source:
            print("Say something!")
            mixer.init()
            mixer.music.load('chime1.mp3')
            mixer.music.play()
            try:
                audio = r.listen(source, timeout=5)
                mixer.music.load('chime2.mp3')
                mixer.music.play()

            except sr.WaitTimeoutError as e:
                print("Timeout; {0}".format(e))
            else:
                pass
            with open("Audio_recognizer_voice.wav", "wb") as f:
                f.write(audio.get_wav_data())
        temp=[]
        y, sar = librosa.load('Audio_recognizer_voice.wav')
        audio_data, _ = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        mfcc_features = mfcc(audio_data)
        temp.append(['Audio_recognizer_voice', [mfcc_features]])

        with open('voice.obj', 'wb') as f:
            pickle.dump(temp, f)

        with open('voice.obj', 'rb') as f:
            object_file = pickle.load(f)

            # converting lists to pandas data frame buffer
            df = pd.DataFrame(object_file, columns=['label', 'data'])
            x_data = df['data']
            X = []
            for x in x_data:
                X.append(x[0])

        X = np.array(X)
        X = pad_sequences(X, 3001)
        print(X.shape)
        X_data = X.reshape(X.shape[0], X.shape[1], X.shape[2], 1)
        # load json and create model

        json_file = open('relu_15_sgd.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        # load weights into new model
        loaded_model.load_weights("relu_15_sgd.h5")
        print("Loaded model from disk")
        ynew = loaded_model.predict([X_data])
        result = np.argmax(ynew)
        print(result)

        conn = sqlite3.connect('kashmir_TEXT_DB')
        c = conn.cursor()
        c.execute("SELECT Text FROM Ktext_TABLE WHERE rowid IS {}".format(str(result)))
        word = c.fetchone()
        print(word)
        entry_text_to_say.delete('0', tk.END)
        entry_text_to_say.insert(0, word)
        os.remove('Audio_recognizer_voice.wav')

label1_say = ttk.Label(root, text='You Said:', font=(f1))
label1_say.grid(row=10,rowspan=2, column=0,sticky=W)

MyButton_rec = Button(root, image=photo,command=listen,font=(f1))#, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton_rec.grid(row=15, column=5,sticky=W)

e1 = entry_text_to_say = ttk.Entry(root, width=20,font=(f1))
entry_text_to_say.grid(row=10,rowspan=2, column=3, columnspan=5,sticky=W)

mainloop()