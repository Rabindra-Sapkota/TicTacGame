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
    def gameBoard(self):
        return self.game_board

    #function to clear gameboard at start/restart of game
    def cleardboard(self):
        self.game_board = {1:'',2:'',3:'',4:'',5;'',6:'',7:'',8:'',9:''}