import time
import os
import speech_recognition as sr
from queue import Queue

#this dosen't work for python 3.13+
class stt:
    def __init__(self):
        self.result_queue = Queue()
    def convert(self):
        try:
            time.sleep(0.2)
            # Initialize the recognizer
            recognizer = sr.Recognizer()

            # Open the audio file
            with sr.AudioFile("temp_input.wav") as source:
                # Record the audio data
                audio_data = recognizer.record(source)

                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data)
            
            os.remove("temp_input.wav")
            return text
        except Exception as e:
            print(e)
            return '...'
    


''' alternative for python 3.13+ (recommended to use python 3.12.7 and below)
import pocketsphinx
import time

class stt :
    def convert(self):
        time.sleep(0.2)  # Optional: If you want to add a delay before processing

        # Set model paths
        model_path2 = r"D:\Documents\python projects\(proj. 10)AI_waifu_V2\version 1.0(async_cai, unreal_engine)\venv\Lib\site-packages\pocketsphinx\model\en-us\en-us"
        model_path = r"D:\Documents\python projects\(proj. 10)AI_waifu_V2\version 1.0(async_cai, unreal_engine)\venv\Lib\site-packages\pocketsphinx\model\en-us"

        # Create a decoder with the specified models
        config = pocketsphinx.Decoder.default_config()
        config.set_string('-hmm', model_path2)  # Acoustic model path
        config.set_string('-lm', model_path + '/en-us.lm.bin')  # Language model path
        config.set_string('-dict', model_path + '/cmudict-en-us.dict')  # Dictionary path

        # Initialize the decoder
        decoder = pocketsphinx.Decoder(config)

        # Decode audio file
        audio_file = 'input.wav'
        try:
            with open(audio_file, 'rb') as f:
                decoder.start_utt()  # Start utterance
                while True:
                    buf = f.read(1024)  # Read in chunks
                    if not buf:
                        break
                    decoder.process_raw(buf, False, False)  # Process the audio buffer
                decoder.end_utt()  # End the utterance

            # Get the result
            hypothesis = decoder.hyp()
            if hypothesis is not None:
                text = hypothesis.hypstr  # Extract recognized text
                return text
            else:
                return "No speech recognized."
        except Exception as e:
            return f"Error processing audio: {e}"

'''
