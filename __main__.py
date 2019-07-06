import pygame
from game import Game

SIZE_X = 1000
SIZE_Y = 1000

if __name__ == '__main__':
    pygame.font.init()
    pygame.init()

    pygame.display.set_mode((SIZE_X, SIZE_Y))

    pygame.display.set_caption('racingGame')
    background = pygame.image.load("racetrack.png").convert_alpha()

    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    clock = pygame.time.Clock()

    game = Game(SIZE_X, SIZE_Y, background)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game.tick()
        game.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
