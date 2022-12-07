import pygame
import random


class Spider(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/spider.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.velocity = random.randint(7,11)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(2,926)
        self.degat = 1

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
            if self.rect.y >= 560:
                self.rect.y = 0
                self.rect.x = random.randint(2,926)
                self.game.add_score(1)
        else:
            self.game.player.damage(self.degat)
