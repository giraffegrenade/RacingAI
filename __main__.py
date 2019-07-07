import pygame
import ctypes
from game import Game

SIZE_X = 1000
SIZE_Y = 1000

if __name__ == '__main__':
    ctypes.windll.user32.SetProcessDPIAware()

    pygame.font.init()
    pygame.init()

    pygame.display.set_mode((SIZE_X, SIZE_Y))

    pygame.display.set_caption('racingGame')
    background = pygame.image.load("racetrack3.png").convert_alpha()

    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    clock = pygame.time.Clock()

    init_state = True

    game = Game(SIZE_X, SIZE_Y, background)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if init_state:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        game.add_checkpoint(pygame.mouse.get_pos())
                    elif event.button == 3:
                        init_state = False
                        game.add_checkpoint(pygame.mouse.get_pos())
                        game.start()

        if not init_state:
            game.tick()
            game.draw(screen)
        else:
            screen.blit(background, (0, 0))
            game.draw_checkpoints(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
