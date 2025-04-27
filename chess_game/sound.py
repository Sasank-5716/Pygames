import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        move_path = 'assets/move.wav'
        if not os.path.exists(move_path):
            print(f"Sound file {move_path} not found.")
            self.move_sound = None
        else:
            self.move_sound = pygame.mixer.Sound(move_path)
