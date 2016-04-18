from random import randint

class Entity(object):
    def __init__(self, x, y, griddict):
        self.x=x
        self.y=y
        self.egdict=griddict

    def getsymbol(self):
        return " "

    def getmoves(self, basic):
        moves = []
        if basic:
            for i in xrange(-1,2,2):
                possible=(self.x+i,self.y)
                if possible in self.egdict:
                    if isinstance(self.egdict[possible], Empty):
                        moves.append(possible)
                possible=(self.x,self.y+i)
                if possible in self.egdict:
                    if isinstance(self.egdict[possible], Empty):
                        moves.append(possible)
        else:
            for i in xrange(-1,2):
                for j in xrange(-1,2):
                    if (i,j)!=(self.x,self.y):
                        possible=(self.x+i,self.y+j)
                        if possible in self.egdict:
                            if isinstance(self.egdict[possible], Empty):
                                moves.append(possible)
        return moves

    def move(self, basic=True):
        curpos=(self.x,self.y)
        moves = self.getmoves(basic)
        if len(moves)>0:
            index=randint(0,len(moves)-1)
            self.x,self.y=moves[index][0],moves[index][1]
            return moves[index]
        else:
            return curpos

    def getpos(self):
        return (self.x,self.y)
        
                
    def update(self):
        pass
        

class Empty(Entity):
    def __init__(self, x, y, griddict):
        super(Empty, self).__init__(x,y,griddict)

    def move(self):
        pass

class Zombie(Entity):
    def __init__(self, x, y, griddict):
        super(Zombie, self).__init__(x,y,griddict)
        self.symbol="ABCDEFGIJKLMNOPQRSTUWXYZ"[randint(0,23)]

    def getsymbol(self):
        return self.symbol#"Z"

class Victim(Entity):
    def __init__(self, x, y, griddict):
        super(Victim, self).__init__(x,y,griddict)

    def getsymbol(self):
        return "V"

    def move(self, basic=False):
        super(Victim, self).move(basic)

class Hunter(Entity):
    def __init__(self, x, y, griddict):
        super(Hunter, self).__init__(x,y,griddict)
        
    def getsymbol(self):
        return "H"

    def move(self, basic=False):
        super(Hunter, self).move(basic)

class Grid(object):
    def __init__(self, row, col, z, h, v, t):
        self.row=row
        self.col=col
        self.zoms=z
        self.huns=h
        self.vics=v
        self.ticks=t
        self.gdict = {}

    def populate(self):
        z,h,v=0,0,0
        for i in xrange( max([self.zoms,self.huns,self.vics]) ):
            if (self.zoms!=z):
                x,y=randint(0,self.row-1),randint(0,self.col-1)
                while (x,y) in self.gdict:
                    x,y=randint(0,self.row-1),randint(0,self.col-1)
                self.gdict[x,y]=Zombie(x,y,self.gdict)
                z+=1
            if (self.huns!=h):
                x,y=randint(0,self.row-1),randint(0,self.col-1)
                while (x,y) in self.gdict:
                    x,y=randint(0,self.row-1),randint(0,self.col-1)
                self.gdict[x,y]=Hunter(x,y,self.gdict)
                h+=1
            if (self.vics!=v):
                x,y=randint(0,self.row-1),randint(0,self.col-1)
                while (x,y) in self.gdict:
                    x,y=randint(0,self.row-1),randint(0,self.col-1)
                self.gdict[x,y]=Victim(x,y,self.gdict)
                v+=1

        for i in xrange(self.row*self.col):
            x,y=i%self.row,i/self.row
            if (x,y) not in self.gdict:
                self.gdict[x,y]=Empty(x,y,self.gdict)

        #print self.gdict[2,2].getmoves()

    def printgrid(self):
        print "-"+("----"*self.row)
        for y in xrange(self.col):
            print "|",
            for x in xrange(self.row):
                print self.gdict[x,y].getsymbol()+" |",
            print
            print "-"+("----"*self.row)

    def tick(self):
        self.moves()
        self.attacks()
        self.printgrid()

    def moves(self):
        for y in xrange(self.col):
            for x in xrange(self.row):
                newpos = self.gdict[x,y].move()
                #print newpos
                if newpos == (x,y):
                    pass
                else:
                    self.gdict[newpos]=self.gdict[x,y]
                    self.gdict[x,y]=Empty(x,y,self.gdict)

    def attacks(self):
        pass
                

    def loop(self):
        ticks_ran=0
        while ticks_ran<self.ticks:
            self.tick()
            ticks_ran+=1

if __name__=="__main__":
    grid = Grid(5,5,5,5,5,3)
    grid.populate()
    grid.printgrid()

    grid.loop()
