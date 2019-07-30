from Player import ComputerPlayer, HumanPlayer
from helper import letter_to_integer
from random import randint

class Game(object):
    def __init__(self):
        self.player_one, self.player_two = self.__set_up()
        self.turn = self.__who_goes_first()

    def __set_up(self):
        player_one = HumanPlayer()
        if self.wants_random_board():
            player_one.randomly_place_fleet()
        else:
            player_one.place_fleet()

        computer = ComputerPlayer()
        computer.randomly_place_fleet()

        return player_one, computer

    def wants_random_board(self):
        """Checks if the user wants their board to be randomized."""
        ans = input('Do you want a random board? ')
        if len(ans) > 0:
            if ans[0].lower() == 'y':
                return True

        return False

    def __who_goes_first(self):
        """Randomly picks which player will go first."""
        if randint(0, 1):
            return self.player_two

        return self.player_one

    def rotate_player(self):
        """Sets the player who will make the next move."""
        if self.turn.name == 'player':
            self.turn = self.player_two
        else:
            self.turn = self.player_one

    def has_winner(self, computer, player_one):
        """Checks if a player has won."""
        return computer.board.has_all_ships_sank() and player_one.board.has_all_ships_sank()

    def who_won(self, computer, player_one):
        """Prints who won the game."""
        if player_one.board.hit_counter == 17:
            print('The Computer won!')
        else:
            print('You won!')

    def play_again(self):
        """Prompts the user if he/she wants to play agian."""
        again = input('CONTINUE? ')
        again = again.lower()
        return again.startswith('y')


def main():
    # introduction
    print('Welcome to Battleship!')

    game = Game()

    run = True
    while run:
        print('Your board: ')
        game.player_one.board.display()

        print("\n\nThe computer\'s board: ")
        game.player_two.board.display(for_opponent=True)

        player = game.turn
        opponent = game.player_two if player.name == 'player' else game.player_one

        while not game.has_winner(player, opponent):
            if player.name == 'player':
                coordinates = input('Where to attack (i.e, A, 3): ')

                letter_position, x = coordinates.split(',')
                y = letter_to_integer(letter_position)

                opponent.board.hit_or_miss(int(x), y)

                print('The Computer\'s board: ')
                opponent.board.display(for_opponent=True)
            else:
                same_spot = True
                while same_spot:
                    x, y = randint(0, 9), randint(0, 9)
                    same_spot = opponent.board.has_hit_same_spot(x, y)
                else:
                    opponent.board.hit_or_miss(x, y)

                print('Your board: ')
                opponent.board.display(for_opponent=True)

            game.rotate_player()
            player = game.turn
            opponent = game.player_two if player.name == 'player' else game.player_one
        else:
            game.who_won(player, opponent)

        # check if user wants to play again
        if game.play_again():
            game = Game()
        else:
            run = False

    print('Exiting game...')


if __name__ == '__main__':
    import sys
    if sys.version_info.major == 2:
        print('Use Python 3.0 or higher')
        exit()
    main()
