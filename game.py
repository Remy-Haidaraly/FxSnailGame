import pygame
from player import Player
from spider import Spider
from bonus_event import BonusEvent

class Game():
    def __init__(self):
        self.is_playing = False

        ### PLAYER
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.score = 0

        ### SALAD
        self.bonus_event = BonusEvent(self)

        ### Spider
        self.all_spiders = pygame.sprite.Group()
      



    def start(self):
        self.is_playing = True
        self.spawn_spider()
        self.spawn_spider()

    def game_over(self):
        self.all_spiders = pygame.sprite.Group()
        self.player.health = self.player.health_max
        self.score = 0
        self.bonus_event.reset_percent()
        self.is_playing = False




    def spawn_spider(self):
        self.spider = Spider(self)
        self.all_spiders.add(self.spider)



    def add_score(self, point):
        self.score += point

       

    def update(self, screen):

        ### Score
        BLACK = (0, 0, 0)
        font = pygame.font.SysFont("Arial", 16, bold=True)
        score_text = font.render(f"Score : {self.score}", 1, BLACK)
        screen.blit(score_text, (20,20))
        screen.blit(self.player.image, self.player.rect)
        self.bonus_event.update_bar(screen)



        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 2 :
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= 926: 
            self.player.move_right()

        self.all_spiders.draw(screen)
        self.bonus_event.all_salads.draw(screen)

        for spider in self.all_spiders:
            spider.move()

        for salad in self.bonus_event.all_salads:
            salad.move()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    