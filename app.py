
class Game():
    def __init__(self, turn="X", tie=False, winner=None):

        self.turn = turn
        self.tie = tie
        self.winner = winner
        
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac-Toe")

        while not self.winner and not self.tie:

            self.render()
            self.place_piece()
            self.check_for_winner()
            self.check_for_tie

            if not self.winner and not self.tie:
                self.switch_turn()

            self.render()


    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        ## If there is a tie: print("Tie game!")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")
        if self.tie == True:
            print("Tie Game!")

        elif self.winner:
            print(f"{self.winner} wins the game!")

        else:
            print(f"It's player {self.turn}'s turn!")


    def render(self):
        # Call upon print_board
        ## Call upon print_message
        self.print_board()
        self.print_message()


    def place_piece(self):

        while True:
  
            move = input(f"Enter a valid move (example: A1): ").lower()

            if move not in self.board:
                print("Invalid space. Try again.")
                continue

            if self.board[move] is not None:
                print("That space is already taken.")
                continue

            self.board[move] = self.turn
            break

    
    def check_for_winner(self):

        b = self.board

    
        if b['a1'] and (b['a1'] == b['b1'] == b['c1']):
            self.winner = b['a1']

        elif b['a2'] and (b['a2'] == b['b2'] == b['c2']):
            self.winner = b['a2']

        elif b['a3'] and (b['a3'] == b['b3'] == b['c3']):
            self.winner = b['a3']


        elif b['a1'] and (b['a1'] == b['a2'] == b['a3']):
            self.winner = b['a1']

        elif b['b1'] and (b['b1'] == b['b2'] == b['b3']):
            self.winner = b['b1']

        elif b['c1'] and (b['c1'] == b['c2'] == b['c3']):
            self.winner = b['c1']


        elif b['a1'] and (b['a1'] == b['b2'] == b['c3']):
            self.winner = b['a1']

        elif b['c1'] and (b['c1'] == b['b2'] == b['a3']):
            self.winner = b['c1']



    def check_for_tie(self):

        if None not in self.board.values() and self.winner is None:
            self.tie = True


    def switch_turn(self):

        turn_lookup = {
            "X": "O",
            "O": "X"
        }

        self.turn = turn_lookup[self.turn]

game_instance = Game()
game_instance.play_game()




