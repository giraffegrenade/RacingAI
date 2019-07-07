from abc import ABC


class Controller(ABC):
    """
    @return
    """
    def process_response(self, pos, next_checkpoint):
        pass

    def get_view_distance(self):
        return 100

    def get_view_width(self):
        return 3

    def get_view_amount(self):
        return 8
