class Board:
    def __init__(self):
        self.player_view = [['_'] * 10 for x in range(10)]
        self.oppent_view = [['_'] * 10 for x in range(10)]
        self.hit_counter = 0

    def display(self, for_opponent = False):
        print('   {}'.format(' '.join('ABCDEFGHIJ')))
        board = self.oppent_view if for_opponent else self.player_view
        for i, row in enumerate(board):
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
                if self.player_view[ship.x + x][ship.y + y] != '_':
                    return False

        return True

    def place_ship(self, ship):
        row = column = 1

        if ship.alignment == 'v':
            row = ship.length
        else:
            column = ship.length

        for x in range(row):
            for y in range(column):
                self.player_view[ship.x + x][ship.y + y] = ship.code_name

    def has_hit_same_spot(self, x, y):
        spot = self.player_view[x][y]
        return spot == 'X' or spot == 'O'

    def is_ship_here(self, x, y):
        spot = self.player_view[x][y]
        return spot != '_'

    def which_ship_was_hit(self, x, y):
        return self.player_view[x][y]

    def mark_spot_as_hit(self, x, y):
        self.hit_counter = self.hit_counter + 1
        self.player_view[x][y] = 'X'
        self.oppent_view[x][y] = 'X'

    def mark_spot_as_miss(self, x, y):
        self.player_view[x][y] = 'O'
        self.oppent_view[x][y] = 'O'

    def clear(self):
        # TODO: the ship coordinates are not being reset. If issues occur, then update this
        self.player_view = [['_'] * 10 for x in range(10)]
        self.oppent_view = [['_'] * 10 for x in range(10)]
