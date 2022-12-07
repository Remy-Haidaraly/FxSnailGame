import pygame
from bonus import Salad

class BonusEvent:

    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.speed_percent = 20
        self.all_salads = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.speed_percent / 100

    def reset_percent(self):
        self.percent = 0

    def salad_spawn(self):
        self.all_salads.add(Salad(self))
        self.all_salads.add(Salad(self))


    def is_full(self):
        return self.percent >= 100


    def attempt_fall(self):
          if self.is_full():
                self.salad_spawn()
                self.reset_percent()


    def update_bar(self, surface):

        self.attempt_fall()
        self.add_percent()

        # black bar (background)
        BLACK = (0, 0, 0)
        pygame.draw.rect(surface, BLACK, [0,surface.get_height() -20,surface.get_width(),10])


        # green bar
        GREEN = (0, 255, 0)
        pygame.draw.rect(surface, GREEN, [0,surface.get_height() - 20,(surface.get_width() / 100) * self.percent,10 ])