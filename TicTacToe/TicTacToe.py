class TileUsedError(Exception):
    def __init(self, value):
        self.value = value

class Tile(object):
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.currently = " "

    def set_tile(symbol):
        self.currently = symbol
    

class Game(object):
    def __init__(self, player1 = "X", player2 = "O", size = 3):
        self.player1=player1
        self.player2=player2
        self.size=size
        self.grid = ([[Tile(x,y) for x in xrange(size)] 
                              for y in xrange(size)])
        self.game_not_won = True
        self.p1_go=True

    def play(self):
        goes = self.size*self.size
        print "Enter position in form '# #'"
        print "# is 0, 1 or 2"
        self.draw()
        while self.game_not_won:
            if self.p1_go: print "Player 1 enter an X Y coordinate: "
            else: print "Player 2 enter an X Y coordinate: "

            choice_list = [x for x in xrange(self.size)]
            choice = [-1,-1]
            while choice[0] not in choice_list and choice[1] not in choice_list:
                try:
                    choice = raw_input("> ")
                    choice = choice.split()
                    if choice[0].isdigit(): choice[0] = int(choice[0])
                    if choice[1].isdigit(): choice[1] = int(choice[1])

                    if self.grid[choice[0]][choice[1]].currently != " ":
                        raise TileUsedError("Tile used")
                except (IndexError, SyntaxError, TypeError): 
                    print "Bad input!"
                    choice = [-1,-1]
                except TileUsedError:
                    print "This tile is used, pick another."
                    choice = [-1,-1]

            if self.p1_go:
                self.grid[choice[0]][choice[1]].currently = self.player1
                player = self.player1
            else:
                self.grid[choice[0]][choice[1]].currently = self.player2
                player = self.player2

            
            self.draw()

            if self.check_win(player):
                break
            else: self.p1_go = not self.p1_go
            goes-=1
            if goes < 1:
                print "Nobody wins."
                break
                
                
    def check_win(self, player):
        for x in xrange(self.size):
            if  (self.grid[x][0].currently==self.grid[x][1].currently==
                self.grid[x][2].currently==player)or(
                self.grid[0][x].currently==self.grid[1][x].currently==
                self.grid[2][x].currently==player)or(
                self.grid[0][0].currently==self.grid[1][1].currently==
                self.grid[2][2].currently==player)or( 
                self.grid[2][0].currently==self.grid[1][1].currently==
                self.grid[0][2].currently==player):
                #game is won
                if self.p1_go: 
                    print "Player 1 has won the game!"
                else: 
                    print "Player 2 has won the game!"
                self.game_not_won = False
                return True
        return False

    def draw(self):
        print
        y_count = 0
        print " x0  x1  x2"
        print "|---|---|---|"
        for x in xrange(len(self.grid)):
            print "|",
            for y in xrange(len(self.grid[0])):
                print self.grid[y][x].currently,
                print"|",
            print "y%d" % y_count
            print"|---|---|---|"
            y_count+=1

if __name__ == "__main__":
    mygame = Game()
    mygame.play()
