from python_speech_features import mfcc
import numpy as np
import librosa
import pickle
temp = []
###################################################################
for i in range(1,3109):
        y, sr = librosa.load('Male_South\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):

        y, sr = librosa.load('Male_North\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):

        y, sr = librosa.load('shoib\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])
for i in range(1,3109):

        y, sr = librosa.load('Tral\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('female_North\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(1,3109):

        y, sr = librosa.load('Female_center\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

#######################################

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_North_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

##################################################

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Male_South_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

#################################

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Shoib_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])



for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(2001, 3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(2001, 3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(2001, 3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(2001, 3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(2001, 3109):
        y, sr = librosa.load('Audio Synthesis\\Female_North_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

####################

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_South_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_South_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_south_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_South_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_south_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_South_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

###################################

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_speed1.05\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_speed1.10\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_speed1.15\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_speed1.20\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])


for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_volume0.5\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

for i in range(1,3109):
        y, sr = librosa.load('Audio Synthesis\\Female_center_volume0.7\\' + str(i) + '.wav')
        audio, index = librosa.effects.trim(y, top_db=35, frame_length=2048, hop_length=512, ref=np.max)
        print(str(i))
        # extract MFCC and Filter bank features
        #plt.plot(audio)
        #plt.show()
        mfcc_features = mfcc(audio)
        #plt.plot(mfcc_features)
        #plt.show()
        #filter_bank_features = logfbank(audio, nfft=4421)

        # print parameters

        print('\nMFCC:\nNumber of windows =', mfcc_features.shape[0])
        print('Length of each feature =', mfcc_features.shape[1])

        #print('\nFilter bank: \nNumber of windows =', filter_bank_features.shape[0])
        #print('Length of each feature =', filter_bank_features.shape[1])

        # plot the features
        # mfcc_features = mfcc_features.T
        # plt.matshow(mfcc_features)
        # plt.title('MFCC')

        # filter_bank_features = filter_bank_features.T
        # plt.matshow(filter_bank_features)
        # plt.title('Filter bank')
        # plt.show()
        temp.append([str(i), [mfcc_features]])

with open('Features_Dataset_trimmed_mfcc_3108_Samples.obj', 'wb') as f:
 pickle.dump(temp, f)
for x in temp:
 print('-----------------------------------------------------------------')
 print(x)
 print('-----------------------------------------------------------------')
