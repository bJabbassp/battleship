from Player import ComputerPlayer, HumanPlayer


def main():
    # introduction
    print('Welcome to Battleship!')

    # set up the player
    player_one = HumanPlayer()
    player_one.place_fleet()
    print('Your board is positioned as follows: '.upper())
    player_one.board.display_board()

    # set up the computer
    print("\n\nSetting up the Computer\'s board...".upper())
    computer = ComputerPlayer()
    computer.place_fleet()
    computer.board.display_board()
    print('The Computer is ready.')


def play_again():
    while True:
        again = input('CONTINUE? ')
        again = again.lower()
        if again.startswith('y'):
            return True
        else:
            print('EXITING GAME')
            return False


if __name__ == '__main__':
    import sys
    if sys.version_info.major == 2:
        print('Use Python 3.0 or higher')
        exit()
    main()
