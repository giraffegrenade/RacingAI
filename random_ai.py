from controller import Controller
import random
import math
from vector import Vector


class RandomAIController(Controller):
    def process_response(self, pos, next_checkpoint, speed):
        if self.last_x_action == 0:
            self.last_x_action = random.choice((1, -1))
        if self.last_y_action == 0:
            self.last_y_action = random.choice((1, -1))
        if self.last_pos.x == 0 and self.last_pos.y == 0:
            self.last_x_action = random.choice((1, -1))
            self.last_y_action = random.choice((1, -1))

        else:
            if not math.hypot(pos.x - self.last_pos.x, pos.y - self.last_pos.y) < self.last_distance:
                self.last_x_action = random.choice((1, -1))
                self.last_y_action = random.choice((1, -1))

        self.last_pos = pos
        return self.last_x_action, self.last_y_action
