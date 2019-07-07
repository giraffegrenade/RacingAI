from controller import Controller
import random
import math
from vector import Vector


class RandomAIController(Controller):
    def process_response(self, pos, next_checkpoint, view):
        print(RandomAIController.BT.track)

        return 1, 1