import pygame
from human_controller import *
from random_ai import RandomAIController
from vector import Vector
from util import *
from math import *
import random


class Game:
    CHECKPOINT_RAD = 30
    FLICKER_TIME = 200

    def __init__(self, size_x, size_y, bg):
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.players = [Player(size_x/2, size_y/2, HumanController(), self),
                        Player(size_x/2, size_y/2, HumanController2(), self)]
        self.bg = bg
        self.checkpoints = []

        self.flickerer = Game.FLICKER_TIME
        self.shuffled_players = self.players[:]

    def tick(self):
        for player in self.players:
            player.tick()

    def draw(self, surface):
        surface.blit(self.bg, (0, 0))
        self.draw_checkpoints(surface)

        for player in self.players:
            player.draw(surface)

    def draw_checkpoints(self, surface):
        for checkpoint in self.checkpoints:
            colour = pygame.Color("yellow")
            self.flickerer -= 1
            if self.flickerer <= 0:
                shift(self.shuffled_players)
                self.flickerer = Game.FLICKER_TIME
            for player in self.shuffled_players:
                if player.current_checkpoint == self.checkpoints.index(checkpoint):
                    colour = player.col
            pygame.draw.circle(surface, colour, checkpoint, Game.CHECKPOINT_RAD)

    def is_on_track(self, x, y):
        return self.bg.get_at((int(x), int(y))) == (0, 0, 0, 255)

    def add_checkpoint(self, pos):
        self.checkpoints.append(pos)

    def start(self):
        if len(self.checkpoints) == 0:
            raise Exception("No checkpoints added")
        for player in self.players:
            player.pos.x = self.checkpoints[0][0] - Game.CHECKPOINT_RAD
            player.pos.y = self.checkpoints[0][1] - Game.CHECKPOINT_RAD

    def checkpoint_passed(self, current_checkpoint, pos):
        return hypot(self.checkpoints[current_checkpoint][0] - pos[0], self.checkpoints[current_checkpoint][1] - pos[1]) < Game.CHECKPOINT_RAD


class Player:
    MAX_LIN_ACC = 0.5
    MAX_ANG_ACC = 0.01
    DRAG = 0.93
    GRASS_DRAG = 0.7
    ANG_DRAG = 0.5
    WIDTH = 60
    HEIGHT = 30

    def __init__(self, start_x, start_y, controller,  game):
        self.pos = Vector(start_x, start_y)
        self.controller = controller
        self.game = game
        self.img = pygame.transform.scale(pygame.image.load("car.png").convert_alpha(), (Player.WIDTH, Player.HEIGHT))
        self.col = (random.randint(25, 225), random.randint(25, 225), random.randint(25, 225))
        self.img = tint(self.img, self.col)
        self.v = Vector(0, 0)
        self.dir = 0
        self.speed = 0
        self.av = 0
        self.w = 1
        self.h = 1
        self.rot_img = self.img
        self.current_checkpoint = 0

    def tick(self):
        # Get controller input
        linear_acc, angular_acc = self.controller.process_response(self.pos,
                                                                   self.game.checkpoints[self.current_checkpoint])
        linear_acc = clamp(linear_acc, -Player.MAX_LIN_ACC, Player.MAX_LIN_ACC)
        angular_acc = clamp(angular_acc, -Player.MAX_ANG_ACC, Player.MAX_ANG_ACC)

        self.v += Vector(self.v.dir, linear_acc, True)
        self.av += angular_acc
        self.speed += linear_acc
        self.av *= Player.ANG_DRAG
        self.dir += -self.av * self.speed

        self.v = Vector(self.dir, self.speed, True)

        if self.game.is_on_track(*self.get_center()):
            self.speed *= Player.DRAG
        else:
            self.speed *= Player.GRASS_DRAG


        # Update velocity
        self.pos += self.v

        self.pos.x = clamp(self.pos.x, 0, self.game.size_x-self.w)
        self.pos.y = clamp(self.pos.y, 0, self.game.size_y-self.h)

        if self.game.checkpoint_passed(self.current_checkpoint, self.get_center()):
            self.current_checkpoint += 1
            if self.current_checkpoint == len(self.game.checkpoints):
                raise Exception("PLAYER " + str(self.col) + " WON")

    def get_center(self):
        return self.pos.x + self.rot_img.get_size()[0] / 2, self.pos.y + self.rot_img.get_size()[1] / 2

    def draw(self, surface):
        self.rot_img = pygame.transform.rotate(self.img, -(self.v.dir/(2*pi))*360)
        top_left = (self.pos.x - (self.rot_img.get_size()[0] - self.img.get_size()[0])/2, self.pos.y - (self.rot_img.get_size()[1] - self.img.get_size()[1])/2)
        self.w = self.rot_img.get_size()[0]
        self.h = self.rot_img.get_size()[1]
        surface.blit(self.rot_img, top_left)
