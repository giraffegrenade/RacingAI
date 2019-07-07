from controller import Controller
import pygame


class HumanController(Controller):
    """
    @return
    """
    def process_response(self, pos, next_checkpoint, speed):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        if keys[pygame.K_a]:
            x = -1
        if keys[pygame.K_d]:
            x = 1
        if keys[pygame.K_w]:
            y = -1
        if keys[pygame.K_s]:
            y = 1

        return y, x


class HumanController2(Controller):
    """
    @return
    """
    def process_response(self, pos, next_checkpoint, speed):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        if keys[pygame.K_LEFT]:
            x = -1
        if keys[pygame.K_RIGHT]:
            x = 1
        if keys[pygame.K_UP]:
            y = -1
        if keys[pygame.K_DOWN]:
            y = 1

        return y, x

