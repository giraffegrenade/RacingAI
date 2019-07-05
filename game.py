import pygame
from abc import ABC



class Game:
    def __init__(self, size_x, size_y):
        self.size_x = int(size_x)
        self.size_y = int(size_y)

    def tick(self):
        pass

    def draw(self, surface):
        pass


class Player:
    def __init__(self, start_x, start_y, controller):
        self.x = x
        self.y = y
        self.conroller = controller
        self.img = pygame.image.load("car.png");

    def tick(self):
        pass

    def draw(self, surface):
        surface.blit(self.img, self.x, self.y)


class Controller(ABC):
    """
    @return 
    """
    def process_response(self):
        pass
