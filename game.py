#Create a class for game borad

class Gameboard():
    #define constructor for class object which initializes game_board.
    #dictionary is choosen for gameboard as there as fixed 9 place and
    #it will be easier to work as key value pair
    def __init__(self):
        self.game_board = {1:'',2:'',3:'',4:'',5;'',6:'',7:'',8:'',9:''}


    #create set_item function which sets value to users choice position in gameboard
    #setting of value is done by placing user as value on choosen key of dictionary
    #game board is written after setting items
    def set_items(self,user,position,game_board):
        game_board[position]=user
        return game_board

    #gameboard function is used as decorator to update change when dependent variable changes
    @property
    def game_Board(self):
        return self.game_board

    #function to clear gameboard at start/restart of game
    def clear_board(self):
        self.game_board = {1:'',2:'',3:'',4:'',5;'',6:'',7:'',8:'',9:''}

    #function to validate if desired place is already taken
    def is_place_taken(sef,game_board,position):
        if game_board[position] != '':
            return True
        else:
            return False

    #function to check if game board is full after ever insert. Used to show tie if already full
    #it checks every values. false is returned is any of the place is vaccant
    #if no vaccant place is found then loop terminates and true is returned
    def is_board_full(self,game_board):
        for user_values in game_board.values():
            if user_values == '':
                return False
        return  True


    #chech if game_is won after every insert
    def is_game_won(self,game_board):
        win_conditions = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        for win_condition in win_conditions:
            if game_board[win_condition[0]] == game_board[win_condition[1]] == game_board[win_condition[2]] and game_board[win_condition[0]] != '':
                return True