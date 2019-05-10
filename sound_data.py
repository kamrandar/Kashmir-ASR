import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
y = wave.open('1.wav','r')

sample_rate, data = wavfile.read('1.wav')

bit_rate = ((y.getframerate() * y.getsampwidth() * 8 * y.getnchannels()) / 1000)

print(sample_rate)
print(bit_rate)

#plt.plot(data,'g', label='line one', linewidth=1)

plt.plot(data)
#plt.bar(data, color='g', height=10, align='center')

#plt.scatter(data,data)#, align='center')
plt.xlabel("Time")

plt.ylabel("Amplitude")
plt.title("signal for 2.wav of Female_north")
plt.show()
#plt.legend()
#plt.grid(True,color='k')
