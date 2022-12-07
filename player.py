import pygame
from sound import SoundManager


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 1
        self.health_max = 1
        self.velocity = 7
        self.image = pygame.image.load("assets/snail_right.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 400
        self.soundmanager = SoundManager()
        
        
    def move_left(self):
        self.image = pygame.image.load("assets/snail_left.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect.x -= self.velocity

    def move_right(self):
        self.image = pygame.image.load("assets/snail_right.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect.x += self.velocity

    def damage(self, degat):
        self.health -= degat
        if self.health <= 0:
           self.game.game_over()
           self.soundmanager.play('game_over')
