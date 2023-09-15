import pyttsx3
import sounddevice as sd
import soundfile as sf
from rvc_infer import rvc_convert
from tortoise_api import Tortoise_API

def text_to_wav(text, filename, voice_index=0, ):
    engine = pyttsx3.init(driverName='sapi5')
    
    voices = engine.getProperty('voices')
    if voice_index >= len(voices):
        print(f"Invalid voice index. Choose between 0 and {len(voices) - 1}. Using default voice.")
    else:
        engine.setProperty('voice', voices[voice_index].id)
    
    engine.setProperty('rate', 150)
    engine.save_to_file(text, filename)
    engine.runAndWait()

def play_audio(filename):
    data, samplerate = sf.read(filename)
    sd.play(data, samplerate)
    sd.wait()

def tts():
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")

    voice_index = 1
    text = "Hello there, my name is marine and I am excited to meet you!"
    audio_file_name = "out.wav"
    
    text_to_wav(text, 
                audio_file_name, 
                voice_index)
    
    return audio_file_name

if __name__ == "__main__":
    audio_file_name = tts() #returns a path

    print(f"audio file path: {audio_file_name}")
    # play_audio(audio_file_name)
    rvc_convert(model_path="marine.pth",
                f0_up_key=0,
                input_path=audio_file_name)

    

