import asyncio
from edge_tts import Communicate
from modules.functionality.start_speaking import *


class talk:
    def __init__(self,text):
        self.text = text
    async def run(self):

        tts = Communicate(text=self.text, voice="fil-PH-BlessicaNeural")
        await tts.save("temp_output.mp3")

        #speak().begin()

'''
from pyht import Client
from pyht.client import TTSOptions
from modules.functionality.start_speaking import *

class talk:
    def __init__(self,text):
        self.text = text
    def run(self):


        #conversion
        client = Client(
            user_id="5HQSdYB0HWMUJvPSbFNEzBn3xL43",
            api_key="646d6f73939d41dcb6dc24d7867319f2"
        )
        options = TTSOptions(voice="s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json")


        with open('temp_output.wav', 'wb') as f:
            for chunk in client.tts(self.text, options,voice_engine = 'PlayDialog-http'):

            # Write the audio chunk to the file
                f.write(chunk) 

        speak().begin()
'''