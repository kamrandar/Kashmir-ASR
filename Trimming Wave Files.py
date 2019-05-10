import librosa
import numpy as np
import matplotlib.pyplot as plt
y, sr = librosa.load('Female_south\\1.wav')
# Trim the beginning and ending silence
yt, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
mfcc=librosa.feature.mfcc(y=y, sr=sr)
print(yt)
plt.xlabel('Not Trimmed')
plt.show()
plt.plot(yt)
plt.xlabel('Trimmed')
plt.show()