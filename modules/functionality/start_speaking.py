import os
import pygame
from modules.data_handlers.executable_file_redirector import *

class speak:
    def begin(self):
        pygame.init()

        # Load the sound file
        #voice_path = convert().get_audio_file_relative_to_exe('output.mp3')
        sound = pygame.mixer.Sound('temp_output.mp3')

        # Play the sound
        sound.play()

        # Wait for the sound to finish playing
        while pygame.mixer.get_busy():
            pygame.time.wait(100)

        # Delete the file after playing (optional)
        os.remove("temp_output.mp3")
        return