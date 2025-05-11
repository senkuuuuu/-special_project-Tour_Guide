import os
from modules.data_handlers.executable_file_redirector import *

class fetch:
    def __init__(self, directory):
        self.sprites = []
        self.directory = convert().get_resource_path(directory)
        
    def begin(self):
        for filename in os.listdir(self.directory):
            self.sprites.append(self.directory+ '/' + filename)
        return self.sprites