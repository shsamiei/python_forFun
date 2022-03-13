
import random

class tic_toc_toe :
    def __init__(self):
        self.board = []
        pass

    def create_game_board(self):
        for i in range(3):
            col = []
            for j in range(3):
                col.append('-')
            self.board.append(col)
        
    # def get_board(self):
    #     return self.board

    def get_turn_player(self): 
        return random.randint(0, 1)


    def fill_spot(self, row , col , player):
        self.board[row][col] = player
        pass

    def is_player_win(self , player):
        # row 
        win = None
        n = len(self.board)
        for i in range(n) :
            win = True
            for j in range(n):
                if self.board[j][i] != player :
                    win = False
                    break
            if win :
                return win

        
        #col :

        win = None

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player :
                    win = False
                    break
            if win :
                return win
             
        # diagonals  :
        win = True
        for i in range(n):
            if self.board[i][i] != player :
                win = False
        if win : 
            return win
        
        win = True 
        for i in range(n):
            if self.board[n-i-1][i] != player:
                win = False
                break
        if win : 
            return win 

        
        # for row in self.board:
        #     for item in row:
        #         if item == '-':
        #             return False
        # return True


        

    def is_board_fill(self):
        for row in self.board:
            for item in row :
                if item == '-' :
                    return False
        return True


    def change_turn(self , player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board :
            for item in row :
                print(item , end =" ")
            print()

        pass

    def game_start(self):

        self.create_game_board()
        player = 'X' if self.get_turn_player == 1 else 'O'

        while True:
            print(f'player {player} turn : ')
            self.show_board()
            row , col = list(map(int , input("Enter row and column numbers to fix spot: ").split())) 
            self.fill_spot(row - 1 , col -1  , player)

            if(self.is_player_win(player)) :
                print(f'player {player} win the game ! ')
                break
            if self.is_board_fill():
                print("the game is draw ! ")
                break
            
            player = self.change_turn(player)

            print()
            self.show_board()
            pass








game = tic_toc_toe()
# game.create_game_board()
# game.show_board()
game.game_start()


