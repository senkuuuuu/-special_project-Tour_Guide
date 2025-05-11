import pygame
from modules.data_handlers.fetch_sprites import *


class Character:
    def __init__(self):
        #fetching sprites, NOTE: can be upgraded into sprites/character_name/idle
        self.character_idle_sprites = fetch('sprites/idle').begin() 
        self.character_talking_sprites = fetch('sprites/talking').begin()
        self.character_thinking_sprites = fetch('sprites/thinking').begin()

        #fetching buttons
        self.buttons_sprites = fetch('sprites/buttons').begin()

        #setting up background
        self.background = (0,0,0)

        #dimensions
        self.character_dimension = (500, 700)
        self.character_position = (275, 400)

        self.mic_scale = (25, 50)
        self.recording_scale = (50, 50)
        self.mic_N_recording_position = (520, 40)
        

        #loading the pygame image for buttons
        self.mic = pygame.image.load(self.buttons_sprites[0])
        self.mic = pygame.transform.scale(self.mic, self.mic_scale)
        self.mic_rect = self.mic.get_rect(center=(self.mic_N_recording_position))

        self.recording = pygame.image.load(self.buttons_sprites[1])
        self.recording = pygame.transform.scale(self.recording,self.recording_scale)
        self.recording_rect = self.recording.get_rect(center=(self.mic_N_recording_position))

        #initial status of mic
        self.mic_status = self.mic
        self.mic_status_rect = self.mic_rect
    
    def idle(self, screen, character_state):
        if character_state%2 == 0:
            character_image = pygame.image.load(self.character_idle_sprites[0])
        elif character_state%2 != 0:
            character_image = pygame.image.load(self.character_idle_sprites[1])

        character_image = pygame.transform.scale(character_image, self.character_dimension)
        character_image_rect = character_image.get_rect(center=self.character_position)

        screen.fill(self.background)
        screen.blit(character_image, character_image_rect)
        screen.blit(self.mic_status, self.mic_status_rect)
    
    def talking(self, screen, character_state):
        if character_state/3 == 1:
            character_image = pygame.image.load(self.character_talking_sprites[2])
        elif character_state%3 == 0:
            character_image = pygame.image.load(self.character_talking_sprites[0])
        elif character_state%3 != 0:
            character_image = pygame.image.load(self.character_talking_sprites[1])

        character_image = pygame.transform.scale(character_image, self.character_dimension)
        character_image_rect = character_image.get_rect(center=self.character_position)

        screen.fill(self.background)
        screen.blit(character_image, character_image_rect)
    
    def thinking(self, screen):
        character_image = pygame.image.load(self.character_thinking_sprites[0])
        character_image = pygame.transform.scale(character_image, self.character_dimension)
        character_image_rect = character_image.get_rect(center=self.character_position)

        screen.fill(self.background)
        screen.blit(character_image, character_image_rect)

    def button_clicked(self, mousepos):
        result = self.mic_status_rect.collidepoint(mousepos)
        return result
    
    def change_mic(self, type):
        if type == 0:
            self.mic_status = self.recording
            self.mic_status_rect = self.recording_rect
        else:
            self.mic_status = self.mic
            self.mic_status_rect = self.mic_rect

