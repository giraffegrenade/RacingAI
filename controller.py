from abc import ABC
from enum import Enum


class Controller(ABC):
    """
    @return
    """
    def process_response(self, view, distance_next_cp):
        pass

    def get_view_distance(self):
        return 200

    def get_view_width(self):
        return 3

    def get_view_amount(self):
        return 8
