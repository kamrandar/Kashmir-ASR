from AudioLib.AudioProcessing import AudioProcessing
from AudioLib import AudioEffect

# Male North Speed Effect
'''
for i in range(1,3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.05)
    sound1.save_to_file('Audio Synthesis\\Male_North_speed1.05\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.10)
    sound1.save_to_file('Audio Synthesis\\Male_North_speed1.10\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.15)
    sound1.save_to_file('Audio Synthesis\\Male_North_speed1.15\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.20)
    sound1.save_to_file('Audio Synthesis\\Male_North_speed1.20\\'+ str(i) +'.wav')

# Male South Speed Effect

for i in range(1,3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.05)
    sound1.save_to_file('Audio Synthesis\\Male_South_speed1.05\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.10)
    sound1.save_to_file('Audio Synthesis\\Male_South_speed1.10\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.15)
    sound1.save_to_file('Audio Synthesis\\Male_South_speed1.15\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.20)
    sound1.save_to_file('Audio Synthesis\\Male_South_speed1.20\\'+ str(i) +'.wav')

# Female North Speed Effect

for i in range(1,3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.05)
    sound1.save_to_file('Audio Synthesis\\Female_North_speed1.05\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.10)
    sound1.save_to_file('Audio Synthesis\\Female_North_speed1.10\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.15)
    sound1.save_to_file('Audio Synthesis\\Female_North_speed1.15\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.20)
    sound1.save_to_file('Audio Synthesis\\Female_North_speed1.20\\'+ str(i) +'.wav')

# Female South Speed Effect

for i in range(1,3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.05)
    sound1.save_to_file('Audio Synthesis\\Female_South_speed1.05\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.10)
    sound1.save_to_file('Audio Synthesis\\Female_South_speed1.10\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.15)
    sound1.save_to_file('Audio Synthesis\\Female_South_speed1.15\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.20)
    sound1.save_to_file('Audio Synthesis\\Female_South_speed1.20\\'+ str(i) +'.wav')

# Male Center Speed Effect

for i in range(1,3109):
    sound1 = AudioProcessing('shoib\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.05)
    sound1.save_to_file('Audio Synthesis\\shoib_speed1.05\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('shoib\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.10)
    sound1.save_to_file('Audio Synthesis\\shoib_speed1.10\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('shoib\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.15)
    sound1.save_to_file('Audio Synthesis\\shoib_speed1.15\\'+ str(i) +'.wav')
for i in range(1,3109):
    sound1 = AudioProcessing('Shoib\\' + str(i) + '.wav')
    sound1.set_audio_speed(1.20)
    sound1.save_to_file('Audio Synthesis\\Shoib_speed1.20\\'+ str(i) +'.wav')

# Female center Speed Effect

for i in range(1, 3109):
    try:
        sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
        print(str(i))
        sound1.set_audio_speed(1.05)
        sound1.save_to_file('Audio Synthesis\\Female_center_speed1.05\\'+ str(i) +'.wav')
    except ValueError:
        print(str(i)+'omitted')
for i in range(1, 3109):
    try:
        sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
        sound1.set_audio_speed(1.10)
        sound1.save_to_file('Audio Synthesis\\Female_center_speed1.10\\'+ str(i) +'.wav')
    except ValueError:
        print(str(i)+'omitted')
for i in range(1, 3109):
    try:
        sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
        sound1.set_audio_speed(1.15)
        sound1.save_to_file('Audio Synthesis\\Female_center_speed1.15\\'+ str(i) +'.wav')
    except ValueError:
        print(str(i)+'omitted')
for i in range(1, 3109):
    try:
        sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
        sound1.set_audio_speed(1.20)
        sound1.save_to_file('Audio Synthesis\\Female_center_speed1.20\\'+ str(i) +'.wav')
    except ValueError:
        print(str(i)+'omitted')

# Radio Effect

for i in range(1,3109):
    AudioEffect.radio('Female_south\\' + str(i) + '.wav','Audio Synthesis\\Female_South_radio\\'+ str(i) +'.wav')
for i in range(1,3109):
    AudioEffect.radio('Male_south\\' + str(i) + '.wav','Audio Synthesis\\Male_South_radio\\'+ str(i) +'.wav')

for i in range(1,3109):
    AudioEffect.radio('Female_North\\' + str(i) + '.wav','Audio Synthesis\\Female_North_radio\\' + str(i) + '.wav')
for i in range(1,3109):
    AudioEffect.radio('Male_North\\' + str(i) + '.wav', 'Audio Synthesis\\Male_North_radio\\' + str(i) + '.wav')

for i in range(1,3109):
    AudioEffect.radio('Female_center\\' + str(i) + '.wav','Audio Synthesis\\Female_center_radio\\' + str(i) + '.wav')
for i in range(1,3109):
    AudioEffect.radio('Shoib\\' + str(i) + '.wav', 'Audio Synthesis\\Shoib_radio\\' + str(i) + '.wav')

# Eco Effect

for i in range(1,3109):
    AudioEffect.echo('Female_south\\' + str(i) + '.wav','Audio Synthesis\\Female_South_eco0.09\\'+ str(i) +'_echo.wav')
for i in range(1,3109):
    AudioEffect.echo('Male_south\\' + str(i) + '.wav','Audio Synthesis\\Male_South_eco0.09\\'+ str(i) +'_echo.wav')

for i in range(1,3109):
    AudioEffect.echo('Female_North\\' + str(i) + '.wav','Audio Synthesis\\Female_North_eco0.09\\' + str(i) + '_echo.wav')
for i in range(1,3109):
    AudioEffect.echo('Male_North\\' + str(i) + '.wav', 'Audio Synthesis\\Male_North_eco0.09\\' + str(i) + '_echo.wav')

for i in range(1,3109):
    AudioEffect.echo('Female_center\\' + str(i) + '.wav','Audio Synthesis\\Female_center_eco0.09\\' + str(i) + '_echo.wav')
for i in range(1,3109):
    AudioEffect.echo('Shoib\\' + str(i) + '.wav', 'Audio Synthesis\\Shoib_eco0.09\\' + str(i) + '_echo.wav')
'''


# volume 0.7

for i in range(1, 3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    print(str(i)+'MN')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\Male_North_Volume0.7\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    print(str(i) + 'MS')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\Male_South_Volume0.7\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    print(str(i) + 'FN')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\Female_North_Volume0.7\\' + str(i) + '.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    print(str(i) + 'FS')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\Female_South_Volume0.7\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('shoib\\' + str(i) + '.wav')
    print(str(i) + 'MC')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\shoib_Volume0.7\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
    print(str(i) + 'FC')
    sound1.set_volume(0.7)
    sound1.save_to_file('Audio Synthesis\\Female_center_Volume0.7\\' + str(i) + '.wav')

# Volume 0.5

for i in range(1, 3109):
    sound1 = AudioProcessing('Male_North\\' + str(i) + '.wav')
    print(str(i) + 'MN')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\Male_North_Volume0.5\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Male_South\\' + str(i) + '.wav')
    print(str(i) + 'MS')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\Male_South_Volume0.5\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Female_North\\' + str(i) + '.wav')
    print(str(i) + 'FN')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\Female_North_Volume0.5\\' + str(i) + '.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Tral\\' + str(i) + '.wav')
    print(str(i) + 'FS')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\Female_South_Volume0.5\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('shoib\\' + str(i) + '.wav')
    print(str(i) + 'MC')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\shoib_Volume0.5\\'+ str(i) +'.wav')
for i in range(1, 3109):
    sound1 = AudioProcessing('Female_center\\' + str(i) + '.wav')
    print(str(i) + 'FC')
    sound1.set_volume(0.5)
    sound1.save_to_file('Audio Synthesis\\Female_center_Volume0.5\\' + str(i) + '.wav')

