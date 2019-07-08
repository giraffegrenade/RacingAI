from controller import Controller
import random
import math
from vector import Vector
from block_types import BT
from util import clamp


class RandomAIController(Controller):

    REVERSE_THRESHOLD = 1000
    MIN_DISTANCE = 125

    def __init__(self):
        self.view_distance = RandomAIController.MIN_DISTANCE

    def process_response(self, pos, next_checkpoint, view):
        y, x, = -1, 0

        forward = view.vals[1][2]
        backward = view.vals[1][0]
        left = view.vals[1][1]
        right = view.vals[1][3]

        if right is BT.TRACK and not left is BT.TRACK:
            x = 1
        elif left is BT.TRACK and not right is BT.TRACK:
            x = -1
        else:
            x = random.choice((0, 1, -1))
            y = random.choice((-1, 0, 0, 0))

        if (not forward is BT.TRACK or not backward is BT.TRACK) and not left is BT.TRACK and not right is BT.TRACK:
            self.view_distance += 1
        else:
            self.view_distance -= 10

        print(self.view_distance, RandomAIController.REVERSE_THRESHOLD)
        if (self.view_distance >= RandomAIController.REVERSE_THRESHOLD / 2):
            x = 1
            if forward is BT.TRACK:
                y = -1
                x = 0

        return y, x

    def get_view_distance(self):
        self.view_distance = clamp(self.view_distance, RandomAIController.MIN_DISTANCE, RandomAIController.REVERSE_THRESHOLD)
        return self.view_distance

    def get_view_width(self):
        return 2

    def get_view_amount(self):
        return 4
