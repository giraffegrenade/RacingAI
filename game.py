import pygame
from human_controller import HumanController


class Game:
    def __init__(self, size_x, size_y):
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.player = Player(size_x/2, size_y/2, HumanController())

    def tick(self):
        self.player.tick()

    def draw(self, surface):
        self.player.draw(surface)


class Player:
    def __init__(self, start_x, start_y, controller):
        self.x = start_x
        self.y = start_y
        self.controller = controller
        self.img = pygame.image.load("car.png")
        self.vx = 0
        self.vy = 0

    def tick(self):
        # Get controller input

        self.vx = self.controller.vx()

        # Update velocity
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))


