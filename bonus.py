import pygame
import random
from sound import SoundManager


class Salad(pygame.sprite.Sprite):
    def __init__(self, bonus_event):
        super().__init__()
        self.image = pygame.image.load("assets/salad.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.point = 30
        self.bonus_event = bonus_event
        self.velocity = random.randint(7,9)
        self.rect.x = random.randint(2,926)
        self.soundmanager = SoundManager()


    def remove(self):
        self.bonus_event.all_salads.remove(self)

    def move(self):
         self.rect.y += self.velocity
         
         if self.rect.y >= 560:
            self.remove()

         if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_players):
            self.bonus_event.game.add_score(self.point)
            self.soundmanager.play('salad_collision')
            self.remove()