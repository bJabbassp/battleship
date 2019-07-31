
from Ship import Ship
from Board import Board
from random import randint
from helper import letter_to_integer

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.fleet = (
            Ship('carrier', 5),
            Ship('battleship', 4),
            Ship('cruiser', 3),
            Ship('submarine', 3),
            Ship('destroyer', 2)
        )

    def randomly_place_fleet(self):
        for ship in self.fleet:
            alignment = 'v' if randint(0, 1) else 'h'
            ship.set_alignment(alignment)

            while ship.x is None and ship.y is None:
                ship.x = randint(0, 9)
                ship.y = randint(0, 9)
                if self.board.can_place_ship(ship):
                    self.board.place_ship(ship)
                else:
                    ship.x = None
                    ship.y = None

    def get_name(self):
        return self.name

class HumanPlayer(Player):
    def __init__(self):
        super().__init__('Player')

    def place_fleet(self):
        """Places all of the boats on the board. Helper method is the find_spot function."""
        for ship in self.fleet:
            self.find_spot(ship)

    def find_spot(self, ship):
        """Prompts the player where to place the ship on the board and how to align it."""
        self.board.display()
        instructions = 'Place the {}, of a length {}, on the board.'
        print(instructions.format(ship.name, ship.length))

        alignment = None
        while alignment is None:
            alignment = input('Vertical or Horizontal (v/h)? ').lower()
            if alignment != 'v' and alignment != 'h':
                print('v or h?')
                alignment = None
        else:
            ship.set_alignment(alignment)

        placed_ship = False
        while not placed_ship:
            coordinates = input('Enter the starting coordinate for the ship.' +
                             ' Use the form: x, y (e.g. A, 3): ')

            letter_position, x = coordinates.split(',')
            y = letter_to_integer(letter_position)

            ship.set_position(int(x), y)

            if self.board.can_place_ship(ship):
                self.board.place_ship(ship)
                placed_ship = True


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__('Computer')
