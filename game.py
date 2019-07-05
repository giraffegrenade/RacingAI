import pygame
from human_controller import HumanController
from vector import Vector
from util import *
from math import *


class Game:
    def __init__(self, size_x, size_y):
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.player = Player(size_x/2, size_y/2, HumanController())

    def tick(self, keys):
        self.player.tick(keys)

    def draw(self, surface):
        self.player.draw(surface)


class Player:
    MAX_LIN_ACC = 0.01
    MAX_ANG_ACC = 0.1

    def __init__(self, start_x, start_y, controller):
        self.pos = Vector(start_x, start_y)
        self.controller = controller
        self.img = pygame.image.load("car.png")
        self.v = Vector(0, 0)
        self.av = 0

    def tick(self, keys):
        # Get controller input

        linear_acc, angular_acc = self.controller.process_response()
        linear_acc = clamp(linear_acc, -Player.MAX_LIN_ACC, Player.MAX_LIN_ACC)
        angular_acc = clamp(angular_acc, -Player.MAX_ANG_ACC, Player.MAX_ANG_ACC)

        print(self.v, angular_acc)

        self.v += Vector(linear_acc, self.v.dir, True)
        self.v.set_dir(self.v.dir + angular_acc)

        self.v.clamp(0.1)

        # Update velocity
        self.pos += self.v

    def draw(self, surface):
        surface.blit(pygame.transform.rotate(self.img, self.v.dir/(2*pi)*360), tuple(self.pos))


