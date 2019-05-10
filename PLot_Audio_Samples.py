import wave
import numpy as np
import matplotlib.pyplot as plt
import librosa
import utility
np.set_printoptions(threshold=np.nan)
with wave.open('Female_South\\3.wav')as w:
    frames = w.getnframes()
    data = w.readframes(frames)
    channels = w.getnchannels()
    sample_rate=w.getframerate()
    sig = np.frombuffer(data, dtype='B')
    print(sig)
    sig2 = np.frombuffer(sig, dtype='<i2').reshape(-1, channels)
    normalized = utility.pcm2float(sig2, np.float32)
    #(normalized)
    #print(sig2)
    plt.plot(sig2)
    plt.show()
    plt.title('Real Data')

    '''temp= bytearray()

    for i in range(0, len(data), 3):
        temp.append(0)
        temp.extend(data[i:i + 3])
    four_bytes = np.frombuffer(temp, dtype='B').reshape(-1, 4)
    print(four_bytes)
    plt.plot(four_bytes)
    plt.show()
    plt.title('four_bytes')

    sig3 = np.frombuffer(temp, dtype='<i4').reshape(-1, channels)
    print(sig3)
    plt.plot(sig3)
    plt.show()
    plt.title('sig3')'''
