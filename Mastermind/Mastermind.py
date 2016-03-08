import random

class Board(object):
    def __init__(self, rows, columns, pegs):
        self.rows = rows
        self.columns = columns
        self.pegs = pegs
        self.code = self.makeCode()

    def makeCode(self):
        # randomly generate a peg for each row
        code = []
        for i in xrange(self.rows):
            code+= [random.randint(1, self.pegs)]
        return code

    def getCode(self):
        #return the code
        return self.code

    def getColumns(self):
        return self.columns

    def getRows(self):
        return self.rows

    def getPegs(self):
        return self.pegs


class Mastermind(object):
    def __init__(self, board):
        self.board = board

    def play(self):
        # will only loop as many times as there are columns
        #print "Code: %s" % ("").join(map(str,self.board.getCode()))
        tries = self.board.getColumns()
        pegs = self.board.getPegs()
        rows = self.board.getRows()
        code = self.board.getCode()
        print "Can you guess the %d digit number between %s and %s in %d tries?" % ( rows, str(1)*rows, str(pegs)*rows, tries)
        for i in xrange(tries):  
            print "You have %d tries left." % (tries-i)            
            choice = raw_input("> ")
            if len(choice) == self.board.rows: # valid length
                choice = [int(n) for n in list(choice)]
                lastattempt = self.tryCode(choice)
                if lastattempt == "Conratulations!":
                    print lastattempt
                    break
                else:
                    print lastattempt
            
        print "Game is over. Code was %s" % ("").join(map(str,code))
        exit(1)


    def tryCode(self, attempt):
        # copy the code as I will be changing it
        code = list(self.board.getCode())
        #print code
        print attempt
        out, pop = [], []
        if attempt == code:
            return "Congratulations!"
        else:
            # find equal values, they will be removed
            for i in xrange(len(code)):
                if attempt[i] == code[i]:
                    pop+=[i]
                    out+= ["Correct."]
                    
            # removing equal values
            for i in reversed(pop):
                attempt.pop(i)
                code.pop(i)

            # searching through the remaining values for matches
            for i in xrange(len(attempt)):
                for j in xrange(len(code)):
                    if attempt[i] == code[j]:
                        out+=["Right peg."]
                        code.pop(j) 
                        break
            # join up the output
            if (len(out) < 1):
                return "None correct."
            else:
                return (" ").join(out)

if __name__ == "__main__":
    gBoard = Board(4, 10, 6)

    game = Mastermind(gBoard)
    game.play()
    
