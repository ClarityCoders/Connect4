import chalk

class Board():
    def __init__(self):

        self.slots = []
        self.moves_left = 7 * 6
        self.game_over = False
        self.winner = "Draw"

        for i in range(6):
            self.slots.append(["   ", "   ", "   ", "   ", "   ", "   ", "   "])

    def __str__(self):
        board_str = "--1---2---3---4---5---6---7--\n"
        for row in self.slots:
            board_str += "|"
            for item in row:
                board_str += item + "|"
            board_str += "\n-----------------------------\n"
        return board_str


    def pick_move(self, player):
        while True:
            try:
                column = int(input(f"{player.name}, please select a column number to place your piece!"))
            except ValueError:
                print("Sorry, that didn't look like a valid number")
                # better try again... Return to the start of the loop
                continue
            if 1 <= column and column <= 7:
                break
            else:
                print("Sorry, that didn't look like a valid number")
                continue
        
        column -= 1
        for row in range(5, -1, -1):
            if self.slots[row][column] == "   ":
                self.slots[row][column] = f" {player.color(player.letter, bold=True)} "
                self.moves_left -= 1
                if self.check_win(row, column):
                    self.game_over = True
                    self.winner = player.name
                break
    
    def check_win(self, row, column):
        
        # start at 1 because our peice counts!
        consecutive = 1
        currrent_peice = self.slots[row][column]
        startColumn = column
        startRow = row

        # check horizontal going right.
        column += 1
        while column <= 6:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                column += 1
            else:
                break

        # check horizontal going left.
        column = startColumn - 1
        while column >= 0:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                column -= 1
            else:
                break

        if consecutive >= 4:
            return True
        else:
            consecutive = 1

        # check Verticle going up.
        column = startColumn
        row += 1
        while row <= 5:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                row += 1
            else:
                break

        # check Verticle going down.
        row = startRow - 1
        while row >= 0:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                column -= 1
            else:
                break

        if consecutive >= 4:
            return True
        else:
            consecutive = 1

        # check Diagonal South East.
        column = startColumn
        row = startRow
        row += 1
        column += 1
        while row <= 5 and column <= 6:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                row += 1
                column += 1
            else:
                break

        # check Diagonal North West.
        row = startRow - 1
        column = startColumn - 1

        while row >= 0 and column >= 0:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                column -= 1
                row -= 1
            else:
                break

        if consecutive >= 4:
            return True
        else:
            consecutive = 1

        # check Diagonal South West.
        column = startColumn
        row = startRow
        row += 1
        column -= 1
        while row <= 5 and column >= 0:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                row += 1
                column -= 1
            else:
                break

        # check Diagonal North Ease.
        row = startRow - 1
        column = startColumn + 1

        while row >= 0 and column <= 6:
            if self.slots[row][column] == currrent_peice:
                consecutive += 1
                column += 1
                row -= 1
            else:
                break

        if consecutive >= 4:
            return True
        else:
            consecutive = 1

class Player():
    def __init__(self, letter, color):
        self.name = input("What's your name?")
        if len(self.name) > 0:
            self.letter = self.name[0]
        else:
            self.letter = letter
        self.color = color

# Create our board and two players
board = Board()
player1 = Player("B", chalk.Chalk('blue'))
player2 = Player("R", chalk.Chalk('red'))


while not board.game_over:
    print(board)
    if board.moves_left % 2 == 0:
        if board.pick_move(player1):
            print(f"{player1.name} Wins")
    else:
        if board.pick_move(player2):
            print(f"{player2.name} Wins")

print(board)
print(f"{board.winner}!!! You win!")