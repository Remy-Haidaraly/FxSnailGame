import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            "salad_collision": pygame.mixer.Sound("assets/sounds/salad_collision.wav"),
            "game_over" : pygame.mixer.Sound("assets/sounds/game_over.wav")
        } 

    def play(self, name):
        self.sounds[name].play()
