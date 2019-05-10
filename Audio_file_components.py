import struct
import wave

def parse_wave_python(filename):
    with wave.open(filename,'rb') as wave_file:
        sample_rate = wave_file.getframerate()
        number_of_frames=wave_file.getnframes()
        length_in_seconds = wave_file.getnframes() / sample_rate

        first_sample = struct.unpack(
            '<h', wave_file.readframes(1))[0]
        second_sample = struct.unpack(
            '<h', wave_file.readframes(1))[0]
    print('''
Parsed {filename}
-----------------------------------------------
Channels: {num_channels}
Sample Rate: {sample_rate}
First Sample: {first_sample}
Second Sample: {second_sample}
Length in Seconds: {length_in_seconds}
Number of frames:{number_of_frames}
parameters:{get_parameter}'''.format(
        filename=filename,
        num_channels=wave_file.getnchannels(),
        sample_rate=wave_file.getframerate(),
        first_sample=first_sample,
        second_sample=second_sample,
        length_in_seconds=length_in_seconds,
        number_of_frames=number_of_frames,
        get_parameter=wave_file.getparams()))

#for i in range(1,100):
parse_wave_python('Female_south\\1.wav')

