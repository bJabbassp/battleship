class Ship:
    def __init__(self, name, length, code_name):
        self.name = name
        self.code_name = code_name
        self.length = length
        self.x = None
        self.y = None
        self.alignment = None
        self.hp = length

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_alignment(self, alignment):
        self.alignment = alignment

    def has_sank(self):
        return self.hp == 0

    def remove_one_hp(self):
        self.hp = self.hp - 1

    def get_name(self):
        return self.name
