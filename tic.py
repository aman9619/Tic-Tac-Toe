import random 


class Tic_Tac_Toe(object):
    Winning_Combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    )

    WINNERS = ('X-win', 'Draw', 'O-win')

    def __init__(self, BOARD=[]):
        '''
        Initialize the tic tac toe BOARD
        '''
        if len(BOARD) == 0:
            self.BOARD = [0 for i in range(9)]
        else:
            self.BOARD = BOARD

    def Display_BOARD(self):
        '''
        Printing the tic tac toe BOARD
        '''
        for i in range(3):
            print(
                "|| " + str(self.BOARD[i * 3]) +
                " || " + str(self.BOARD[i * 3 + 1]) +
                " || " + str(self.BOARD[i * 3 + 2]) + " ||"
            )

    def checkIfOver(self):
        '''
        Check if the game is over or there is a winner
        '''
        if 0 not in [element for element in self.BOARD]:
            return True
        if self.winner() != 0:
            return True
        return False

    def Possible_Moves(self):
        '''
        To check what all possible moves are remaining for a playr
        '''
        return [index for index, element in enumerate(self.BOARD) if element is 0]

    def Possible_Combinations(self, playr):
        '''
        checking possible places where game can be won
        '''
        return self.Possible_Moves() + self.get_acquired_places(playr)

    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def is_tie(self):
        return self.winner() == 0 and self.checkIfOver()

    def winner(self):
        '''
        check who's the winner

        :return playr: return 'X' or 'O' whoever has won the game
                        else returns 0
        '''
        for playr in ('X', 'O'):
            positions = self.get_acquired_places(playr)
            for combo in self.Winning_Combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return playr
        return 0

    def get_acquired_places(self, playr):
        '''
        To get the positions already acquired by a particular playr

        :param playr: 'X' or 'O'
        '''
        return [index for index, element in enumerate(self.BOARD) if element == playr]

    def Make_Your_Move(self, position, playr):
        self.BOARD[position] = playr

    def min_max(self, node, playr):
        '''
        min_max algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.checkIfOver():
            if node.X_won():
                return -1
            elif node.is_tie():
                return 0
            elif node.O_won():
                return 1
        best = 0
        for move in node.Possible_Moves():
            node.Make_Your_Move(move, playr)
            val = self.min_max(node, get_your_enemy(playr))
            node.Make_Your_Move(move, 0)
            if playr == 'O':
                if val > best:
                    best = val
            else:
                if val < best:
                    best = val
        return best


def DETERMIN(BOARD, playr):
    '''
    Driver function to apply min_max algorithm
    '''
    a = 0
    choices = []
    if len(BOARD.Possible_Moves()) == 9:
        return 4
    for move in BOARD.Possible_Moves():
        BOARD.Make_Your_Move(move, playr)
        val = BOARD.min_max(BOARD, get_your_enemy(playr))
        BOARD.Make_Your_Move(move, 0)
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    try:
        return random.choice(choices)
    except IndexError:
        return random.choice(BOARD.Possible_Moves())


def get_your_enemy(playr):
    if playr == 'X':
        return 'O'
    return 'X'


if __name__ == "__main__":
    BOARD = Tic_Tac_Toe()
    print('BOARD positions are like this: ')
    for i in range(3):
        print(
            "|| " + str(i * 3 + 1) +
            " || " + str(i * 3 + 2) +
            " ||" + str(i * 3 + 3) + " ||"
        )
    print('Type in the position number you to make a move on..')
    while not BOARD.checkIfOver():
        playr = 'X'
        playr_move = int(input("Your turn: ")) - 1
        if playr_move not in BOARD.Possible_Moves():
            print('Check your input!')
            continue
        BOARD.Make_Your_Move(playr_move, playr)
        BOARD.Display_BOARD()
        print()
        if BOARD.checkIfOver():
            break
        print('Computer is making its move... ')
        playr = get_your_enemy(playr)
        machine_move = DETERMIN(BOARD, playr)
        BOARD.Make_Your_Move(machine_move, playr)
        BOARD.Display_BOARD()
    if BOARD.winner() != 0:
        if BOARD.winner() == 'X':
            print (" You are the winner!")
        else:
            print('Computer Won!')
    else:
        print("its a tie!!")
