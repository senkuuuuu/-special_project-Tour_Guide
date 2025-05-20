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
