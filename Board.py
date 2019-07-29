class Board:
    def __init__(self):
        self.board = [['_'] * 10 for x in range(10)]
        self.hit_counter = 0

    def display_board(self):
        print('   {}'.format(' '.join('ABCDEFGHIJ')))
        for i, row in enumerate(self.board):
            print('{}  {}'.format(i, ' '.join(row)))

    def has_all_ships_sank(self):
        if self.hit_counter == 17:
            return True

        return False

    def can_place_ship(self, ship):
        row = column = 1

        if ship.alignment == 'v':
            row = ship.length
        else:
            column = ship.length

        if (ship.x < 0) or \
           (ship.y < 0) or \
           (ship.x + row > 10) or \
           (ship.y + column > 10):
            return False

        for x in range(row):
            for y in range(column):
                if self.board[ship.x + x][ship.y + y] != '_':
                    return False

        return True

    def place_ship(self, ship):
        row = column = 1

        if ship.alignment == 'v':
            row = ship.length
        else:
            column = ship.length

        abrv = ship.name[0]
        for x in range(row):
            for y in range(column):
                self.board[ship.x + x][ship.y + y] = abrv

    def display_oppents_board(self):
        """Prints the players' opponent's board without the boat locations.
        This function modifies the board and calls the display_board function to print the modified board."""
        new_board = list()
        for row in self.game_board:
            with_Bs = '~'.join(row)
            no_Bs = with_Bs.replace('B', '_')
            new_board.append(no_Bs.split('~'))

        self.display_board()
