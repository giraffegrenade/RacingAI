from abc import ABC
from enum import Enum


class Controller(ABC):

    BT = Enum('BT', 'track snow wall')

    """
    @return
    """
    def process_response(self, pos, next_checkpoint, view):
        pass

    def get_view_distance(self):
        return 200

    def get_view_width(self):
        return 3

    def get_view_amount(self):
        return 8
