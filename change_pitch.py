from pydub import AudioSegment
from pydub.playback import play

def change(file_name, pitch):
    sound = AudioSegment.from_file('./wav/' + file_name + '.wav', format="wav")
    octaves = 0.5
    new_sample_rate = int(sound.frame_rate * (pitch ** octaves))

    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    hipitch_sound.export("./wav/out.wav", format="wav")