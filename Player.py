
from Ship import Ship
from Board import Board
from random import randint


class Player:
    def __init__(self):
        self.board = Board()
        self.fleet = (
            Ship('carrier', 5),
            Ship('battleship', 4),
            Ship('cruiser', 3),
            Ship('submarine', 3),
            Ship('destroyer', 2)
        )


class HumanPlayer(Player):
    def place_fleet(self):
        """Places all of the boats on the board. Helper method is the find_spot function."""
        for ship in self.fleet:
            self.find_spot(ship)

    def find_spot(self, ship):
        """Prompts the player where to place the ship on the board and how to align it.
        Helper method is the place_boat function."""
        self.board.display_board()
        instructions = 'Place the {}, of a length {}, on the board.'
        print(instructions.format(ship.name, ship.length))

        alignment = None
        while alignment is None:
            alignment = input('Vertical or Horizontal (v/h)? ')
            if alignment != 'v' and alignment != 'h':
                print('v or h?')
                alignment = None
        else:
            ship.set_alignment(alignment)

        position = None
        while position is None:
            position = input('Enter the starting coordinate for the ship.' +
                             ' Use the form: x, y (e.g. A, 3): ')
            letter_position, x = position.split(',')
            table = str.maketrans('ABCDEFGHIJ', '0123456789')
            y = letter_position.translate(table)
            x, y = map(int, [x, y])
            ship.set_position(x, y)
            if self.board.can_place_ship(ship):
                self.board.place_ship(ship)
            else:
                position = None


class ComputerPlayer(Player):
    def place_fleet(self):
        for ship in self.fleet:
            self.find_spot(ship)

    def find_spot(self, ship):
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
