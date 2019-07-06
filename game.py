import pygame
from human_controller import HumanController
from vector import Vector
from util import *
from math import *


class Game:
    def __init__(self, size_x, size_y):
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.player = Player(size_x/2, size_y/2, HumanController(), self)

    def tick(self):
        self.player.tick()

    def draw(self, surface):
        self.player.draw(surface)


class Player:
    MAX_LIN_ACC = 0.5
    MAX_ANG_ACC = 0.01
    DRAG = 0.95
    ANG_DRAG = 0.5
    WIDTH = 60
    HEIGHT = 30

    def __init__(self, start_x, start_y, controller,  game):
        self.pos = Vector(start_x, start_y)
        self.controller = controller
        self.game = game
        self.img = pygame.transform.scale(pygame.image.load("car.png"), (Player.WIDTH, Player.HEIGHT))
        self.v = Vector(0, 0)
        self.dir = 0
        self.speed = 0
        self.av = 0
        self.w = 1
        self.h = 1

    def tick(self):
        # Get controller input
        linear_acc, angular_acc = self.controller.process_response()
        linear_acc = clamp(linear_acc, -Player.MAX_LIN_ACC, Player.MAX_LIN_ACC)
        angular_acc = clamp(angular_acc, -Player.MAX_ANG_ACC, Player.MAX_ANG_ACC)

        # print(self.v, angular_acc)
        self.v += Vector(self.v.dir, linear_acc, True)
        self.av += angular_acc
        self.speed += linear_acc
        self.av *= Player.ANG_DRAG
        self.dir += -self.av * self.speed

        self.v = Vector(self.dir, self.speed, True)
        self.speed *= Player.DRAG

        # print(self.v)

        # Update velocity
        self.pos += self.v

        self.pos.x = clamp(self.pos.x, 0, self.game.size_x-self.w)
        self.pos.y = clamp(self.pos.y, 0, self.game.size_y-self.h)

    def draw(self, surface):
        rot_img = pygame.transform.rotate(self.img, -(self.v.dir/(2*pi))*360)
        top_left = (self.pos.x - (rot_img.get_size()[0] - self.img.get_size()[0])/2, self.pos.y - (rot_img.get_size()[1] - self.img.get_size()[1])/2)
        self.w = rot_img.get_size()[0]
        self.h = rot_img.get_size()[1]
        surface.blit(rot_img, top_left)
