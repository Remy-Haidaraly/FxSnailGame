import pygame
from game import Game

pygame.init()

BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND_rect = BACKGROUND.get_rect()
WIDTH, HEIGHT = BACKGROUND.get_width(), BACKGROUND.get_height()

pygame.display.set_caption("FxSnailGame")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
screen = pygame.display.set_mode((WIDTH,HEIGHT))


banner = pygame.image.load("assets/menu_snail.png")
banner = pygame.transform.scale(banner, (100,100))
banner_rect = banner.get_rect()
banner_rect.x = 450
banner_rect.y = 350


button_play = pygame.image.load("assets/play.png")
button_play = pygame.transform.scale(button_play, (200,200))
button_play_rect = button_play.get_rect()
button_play_rect.x = WIDTH // 2 - button_play.get_width() // 2
button_play_rect.y = HEIGHT // 2 - button_play.get_height() // 2



FPS = 60
run = True
clock = pygame.time.Clock()
game = Game()

while run:
    clock.tick(FPS)
    screen.blit(BACKGROUND, (0,0))

    if game.is_playing == True:
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(button_play,button_play_rect)
        

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_play_rect.collidepoint(event.pos) and game.is_playing == False:
                game.start()
                