from Player import ComputerPlayer, HumanPlayer
from helper import letter_to_integer, parse_coordinates
from random import randint
from time import sleep

class Game(object):
    def __init__(self):
        self.player_one, self.player_two = self.__set_up()

    def __set_up(self):
        player_one = HumanPlayer()
        if self.wants_random_board():
            player_one.randomly_place_fleet()
        else:
            player_one.place_fleet()

        computer = ComputerPlayer()
        computer.randomly_place_fleet()

        return player_one, computer

    def who_goes_first(self):
        if randit(0, 1):
            return [self.player_one, self.player_two]

        return [self.player_two, self.player_one]

    def wants_random_board(self):
        """Checks if the user wants their board to be randomized."""
        ans = input('Do you want a random board? ')
        if len(ans) > 0:
            if ans[0].lower() == 'y':
                return True

        return False

    def has_winner(self):
        """Checks if a player has won."""
        return self.player_one.board.has_all_ships_sank() or self.player_two.board.has_all_ships_sank()

    def who_won(self):
        """Prints who won the game."""
        if self.player_one.board.hit_counter == 17:
            print('The Computer won!')
        else:
            print('The Player won!')

    def play_again(self):
        """Prompts the user if he/she wants to play agian."""
        again = input('CONTINUE? ')
        again = again.lower()
        return again.startswith('y')

    def get_players(self):
        return [self.player_one, self.player_two]


def main():
    # introduction
    print('Welcome to Battleship!')

    game = Game()

    run = True
    while run:
        print(f"{game.player_one.get_name()} board:")
        game.player_one.board.display()

        sleep(2)
        input(f"\n\nThe {game.player_two.get_name()} is ready! Press enter to continue...")
        sleep(1)

        playing, waiting = game.who_goes_first()
        print(f"The {playing.get_name()} will go first...\n")

        while not game.has_winner():
            hit_same_spot = True
            while hit_same_spot:
                if playing.get_name() == 'Player':
                    coordinates = False
                    while not coordinates:
                        coordinates = parse_coordinates(
                                    input('Where to attack (i.e, A, 3): ')
                                )
                        if coordinates:
                            x, y = coordinates
                        else:
                            print('Bad coordinates')
                else:
                    x, y = randint(0, 9), randint(0, 9)

                hit_same_spot = waiting.board.has_hit_same_spot(x, y)
            else:
                message = waiting.board.hit_or_miss(x, y)

            print(f'{message}! The {waiting.name}\'s board: ')
            waiting.board.display(for_opponent=True)

            # rotate players
            playing, waiting = waiting, playing
        else:
            game.who_won()

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
