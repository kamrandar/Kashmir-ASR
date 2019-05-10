from tkinter import *
from tkinter import ttk
import tkinter as tk
from pygame import mixer
from tkinter import messagebox
import os
import time
#from pyaudio import *
import speech_recognition as sr
import sqlite3

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

def save_file():
    if len(text_serial.get()) == 0:
        messagebox.showinfo("Error", "Enter Speaker's Name")
    else:
        list = os.listdir(emo.get())
        os.rename('microphone-results.wav', emo.get() + "/" + e2.get() + ".wav")
        messagebox.showinfo("Saved", "Audio Saved as : " + emo.get() + "/" + e2.get() + str(len(list)))
        conn = sqlite3.connect('kashmir_TEXT_DB')
        c = conn.cursor()
        sno = e2.get()
        text_box = e1.get()
        c.execute("UPDATE Ktext_TABLE SET  " + emo.get() + " = 1 WHERE s_no = ? AND Text = ?", (sno,text_box))
        conn.commit()
        c.close()
        conn.close()


def listen():
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
                global audio
                audio = r.listen(source, timeout=5)
                mixer.music.load('chime2.mp3')
                mixer.music.play()

            except sr.WaitTimeoutError as e:
                print("Timeout; {0}".format(e))
            else:
                pass
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())


def playaudio():
    try:
        os.system('start microphone-results.wav')
    except:
        print("No Audio File Found")



def Fetch():
    conn = sqlite3.connect('kashmir_TEXT_DB')
    c = conn.cursor()
    c.execute('SELECT Text,s_no FROM Ktext_TABLE WHERE '+emo.get()+' ISNULL')
    data1 = c.fetchone()
    text = data1[0]
    entry_text_to_say.delete('0',tk.END)
    entry_text_to_say.insert(0, text)
    sno = data1[1]
    text_serial.delete('0',tk.END)
    text_serial.insert(0, sno)
    c.close()
    conn.close()
    btn_next = Button(root, text='Next', font=(f1), command=move_next)
    btn_next.grid(row=5, column=4)


def move_next():
    conn = sqlite3.connect('kashmir_TEXT_DB')
    c = conn.cursor()
    c.execute('SELECT Text,s_no FROM Ktext_TABLE WHERE '+emo.get()+' ISNULL')
    data1 = c.fetchone()
    text = data1[0]
    entry_text_to_say.delete('0',tk.END)
    entry_text_to_say.insert(0, text)
    sno = data1[1]
    text_serial.delete('0',tk.END)
    text_serial.insert(0, sno)
    c.close()
    conn.close()

def del_default_rec():
    if os.path.isfile('microphone-results.wav'):
        os.remove('microphone-results.wav')
        messagebox.showinfo("File Deleted","Record Again Please!")
    else:
        messagebox.showinfo("No File Found","NO microphone-results.wav file created Yet")

label1_say = ttk.Label(root, text='SAY WORD:', font=(f1))
label1_say.grid(row=0,rowspan=2, column=0,sticky=W)

label_speaker_name = ttk.Label(root, text='Speaker Name:',font=(f1))
label_speaker_name.grid(row=3, rowspan=2, column=0,sticky=W)

e1 = entry_text_to_say = ttk.Entry(root, width=20,font=(f1))
entry_text_to_say.grid(row=0,rowspan=2, column=1, columnspan=2,sticky=W)

e2 = text_serial = ttk.Entry(root, width=20,font=(f1))
text_serial.grid(row=3,rowspan=2, column=1,sticky=W)

emo = StringVar(root)
emo.set('Male_North')
Dilect_mnu = OptionMenu(root, emo, "Male_North", "Female_North", "Male_center", "female_center", "Male_South", "Female_South","Kamran_sopore","Shoib","Tral")
Dilect_mnu.grid(row=4, column=3)

MyButton_start_rec = Button(root ,text='start',command=Fetch,font=(f1))
MyButton_start_rec.grid(row=5,column=3,sticky=W)


MyButton_sav = Button(root, text='Save Audio', width=20,command=save_file,font=(f1))
MyButton_sav.grid(row=5,column=0,sticky=W)

MyButton_play = Button(root, text='Delete', width=10,command=del_default_rec,font=(f1))
MyButton_play.grid(row=5, column=6, sticky=E)


MyButton_play = Button(root, text='Play', width=20,command=playaudio,font=(f1))
MyButton_play.grid(row=5, column=1, sticky=W)

MyButton_rec = Button(root, image=photo,command=listen,font=(f1))#, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton_rec.grid(row=0, column=3,sticky=W)

mainloop()