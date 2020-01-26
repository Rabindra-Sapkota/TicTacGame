#Create a class for game borad

class Gameboard():
    #define constructor for class object which initializes game_board.
    #dictionary is choosen for gameboard as there as fixed 9 place and
    #it will be easier to work as key value pair
    def __init__(self):
        self.game_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}


    #create set_item function which sets value to users choice position in gameboard
    #setting of value is done by placing user as value on choosen key of dictionary
    #game board is written after setting items
    def set_items(self,symbol,position,game_board):
        game_board[position]=symbol
        return game_board

    #gameboard function is used as decorator to update change when dependent variable changes
    @property
    def game_Board(self):
        return self.game_board

    #function to clear gameboard at start/restart of game
    def clear_board(self):
        self.game_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

    #function to validate if desired place is already taken
    def is_place_taken(sef,game_board,position):
        if game_board[position] != ' ':
            return True
        else:
            return False

    #function to check if game board is full after ever insert. Used to show tie if already full
    #it checks every values. false is returned is any of the place is vaccant
    #if no vaccant place is found then loop terminates and true is returned
    def is_board_full(self,game_board):
        for board_value in game_board.values():
            if board_value == ' ':
                return False
        return  True


    #chech if game_is won after every insert
    def is_game_won(self,game_board):
        win_conditions = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        for win_condition in win_conditions:
            if game_board[win_condition[0]] == game_board[win_condition[1]] == game_board[win_condition[2]] and game_board[win_condition[0]] != ' ':
                return True
        else:
            return False

    def print_board(self,game_board):
        index=1
        for row in range(0,3):
            for column in range(0,3):
                if column != 2:
                    print(game_board[index],end='|')
                else:
                    print(game_board[index])
                index += 1
            if row != 2:
                print('-----')



class Game():
# 1 Game Start
    def start_game(self):
        self.control_board = Gameboard()
        self.game_board = self.control_board.game_board
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print("\t\t\t\t\t\t\t\t\t\t\t***************************")
        print("\t\t\t\t\t\t\t\t\t\t\t**  Welcome To X-O Game  **")
        print("\t\t\t\t\t\t\t\t\t\t\t***************************")
        self.player_one_name=input("Please Enter Player One Name : ")
        self.player_two_name=input("Please Enter Player Two Name : ")
        print('\nHere each place in board is representd as 1-9 starting from left along row')
        self.control_board.print_board(self.game_board)
        self.turn = 1

#2 Game Restart
    def restart_game(self):
        self.control_board = Gameboard()
        self.game_board=self.control_board.game_board
        self.control_board.print_board(self.game_board)
        self.turn = 1

#3 Game end and play again
    def end_game(self):
        if self.game_running == False:
            try:
                replay = int(input('Press 0 to quit or 1 to play again:'))
                if (replay != 0 and replay != 1):
                    raise Exception
                elif replay == 1:
                    self.game_running = True
                    self.restart_game()
            except:
                self.end_game()

#4 Game Turn
    def take_turn(self,user_name,symbol):
        try:
            position = int(input(user_name + ' choose a place, 1-9 : '))
            if position > 9 or position < 1:
                raise Exception
        except:
            print("Pick Number between 1-9 : ")
            return self.take_turn(user_name,symbol)

        if self.control_board.is_place_taken(self.game_board,position):
            print("This place is taken")
            self.take_turn(user_name,symbol)
        else:
            self.control_board.set_items(symbol,position,self.game_board)
            self.control_board.print_board(self.game_board)

        if self.control_board.is_game_won(self.game_board):
            print(user_name + " Wins.")
            self.game_running = False

#4 Game Mamager
    def main(self):
        self.game_running = True
        self.start_game()
        while self.game_running:
            if self.turn % 2 != 0:
                self.take_turn(self.player_one_name,'O')
            else:
                self.take_turn(self.player_two_name,'X')

            if self.control_board.is_board_full(self.game_board) and self.game_running:
                print("Game Draw")
                self.game_running = False
            self.turn += 1

            if not self.game_running:
                self.end_game()

#Create Game Launcher

if __name__ == '__main__':
    a=Game()
    a.main()