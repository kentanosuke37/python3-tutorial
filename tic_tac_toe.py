import random

class Tic_Tac_Tone(object):
    """Short summary.

    Attributes
    ----------
    board : list
        board of Tic Tac Tone
    player1_marker : str
        marker of player 1
    player2_marker : str
        marker of player 2
    turn : str
        string meaning turn of player ---> 'Player 1' or 'Player 2'
    game_on : bool
        If the game is going on, True otherwise False
    """

    def __init__(self):
        """constructor

        Returns
        -------
        None

        """

        self.board = [' '] * 10
        self.player1_marker = None
        self.player2_marker = None
        self.turn = None
        self.game_on = None

        self.decide_markers()

        self.set_first_turn()

        self.show_board_numbers()

    def display_board(self):
        """Displaying a current board

        Returns
        -------
        None

        """

        board = ('   |   |   \n'
                 ' {7} | {8} | {9} \n'
                 '   |   |   \n'
                 '-----------\n'
                 '   |   |   \n'
                 ' {4} | {5} | {6} \n'
                 '   |   |   \n'
                 '-----------\n'
                 '   |   |   \n'
                 ' {1} | {2} | {3} \n'
                 '   |   |   \n').format(*self.board)

        print(board)

    def show_board_numbers(self):
        """Displaying board numbers

        Returns
        -------
        None

        """

        board = ('   |   |   \n'
                 ' 7 | 8 | 9 \n'
                 '   |   |   \n'
                 '-----------\n'
                 '   |   |   \n'
                 ' 4 | 5 | 6 \n'
                 '   |   |   \n'
                 '-----------\n'
                 '   |   |   \n'
                 ' 1 | 2 | 3 \n'
                 '   |   |   \n').format(*self.board)

        print("=== This is the board number ===")
        print(board)

    def decide_markers(self):
        """Deciding player markers

        Returns
        -------
        None

        """
        marker = ''

        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            self.player1_marker = 'X'
            self.player2_marker = 'O'
        else:
            self.player1_marker = 'O'
            self.player2_marker = 'X'

        print('Player 1 ==> {}, Player 2 ===> {}'.format(self.player1_marker, self.player2_marker))

    def place_marker(self):
        """Placing marker considering player turn

        Returns
        -------
        None

        """
        position = self.player_choice()

        if self.turn == 'Player 1':
            self.board[position] = self.player1_marker
        else:
            self.board[position] = self.player2_marker

    def win_check(self):
        """Checking the state of the board, that is, whether player1 or player2 wins or not.

        Returns
        -------
        None

        """

        if self.turn == 'Player 1':
            mark = self.player1_marker
        else:
            mark = self.player2_marker

        # across the top
        if (self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) :
            return True

        # across the middle
        elif (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) :
            return True

        # across the middle
        elif (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) :
            return True

        # across the bottom
        elif (self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) :
            return True

        # down the middle
        elif (self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) :
            return True

        # down the middle
        elif (self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) :
            return True

        # down the right side
        elif (self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) :
            return True

        # diagonal
        elif (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) :
            return True

        # diagonal
        elif (self.board[9] == mark and self.board[5] == mark and self.board[1] == mark) :
            return True

        else:
            return False


    def change_turn(self):
        """Changing turn of players

        Returns
        -------
        None

        """

        if self.turn == 'Player 1':
            self.turn = 'Player 2'
        else:
            self.turn = 'Player 1'

    def set_first_turn(self):
        """Setting the first turn of the game

        Returns
        -------
        None

        """
        if random.randint(0, 1) == 0:
            self.turn = 'Player 2'
        else:
            self.turn = 'Player 1'

        print('{} will go first.'.format(self.turn))

    def space_check(self, position):
        """Checking whether the position of the board is no-marker or not

        Parameters
        ----------
        position : int
            the position of the board

        Returns
        -------
        bool
           if the position is no-marker, True otherwise False

        """
        return self.board[position] == ' '

    def full_board_check(self):
        """Checking whether the board is full of markers or not

        Returns
        -------
        bool
           if the board is full, True otherwise False

        """
        for i in range(1,10):
            if self.space_check(i):
                return False
        return True

    def player_choice(self):
        """Choosing the position of the marker

        Returns
        -------
        int
            the number of position

        """
        position = 0

        if self.turn == 'Player 1':
            display =  'Choose {} ==> {} next position : (1-9) '.format(self.turn, self.player1_marker)
        else:
            display =  'Choose {} ==> {} next position : (1-9) '.format(self.turn, self.player2_marker)

        while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(position):
            try:
                position = int(input(display))
            except ValueError:
                position = -1

        return position

    def replay(self):
        """Asking a need of replaying a game

        Returns
        -------
        str
            if the game will continue, returning 'y' otherwise None

        """
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


    def is_ready_to_start(self):
        """Asking the preparation of the game. If you enter yes,
           game_on is True and then the game will start

        Returns
        -------
        None

        """
        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower().startswith('y'):
            self.game_on = True
        else:
            self.game_on = False

    def is_on_going(self):
        """Asking whether the game is on-going or not

        Returns
        -------
        bool
            If game is on-going, returning True otherwise False

        """
        return self.game_on

    def progress(self):
        """Progressing the game

        Returns
        -------
        None

        """

        self.display_board()

        self.place_marker()

        if self.win_check():
            self.display_board()
            print('{} has won!'.format(self.turn))
            self.game_on = False

        elif self.full_board_check():
            self.display_board()
            print('The game is a draw!')
            self.game_on = False

        else:
            self.change_turn()

    @classmethod
    def start(cls):
        """Starting 'Tic Tac Tone' game

        Parameters
        ----------
        cls : Tic_Tac_Tone class
            Tic_Tac_Tone class object

        Returns
        -------
        None

        """
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            game_ins = cls()

            game_ins.is_ready_to_start()

            while game_ins.is_on_going():
                game_ins.progress()

            if not game_ins.replay():
                break

if __name__ == '__main__':
    Tic_Tac_Tone.start()
