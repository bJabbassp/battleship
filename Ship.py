class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.x = None
        self.y = None
        self.alignment = None

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_alignment(self, alignment):
        self.alignment = alignment
