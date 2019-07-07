class View:
    def __init__(self, distance, width, amount, speed):
        self.distance = distance
        self.width = width
        self.amount = amount
        self.speed = speed
        self.vals = [[False for _ in range(width)] for _ in range(amount)]

    def store(self, dir_index, distance_index, val):
        self.vals[dir_index][distance_index] = val

    def __str__(self):
        return str(self.vals)