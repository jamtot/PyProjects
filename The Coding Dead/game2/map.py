from square import Square
import random

class Map(object):
    def __init__(self, zombs, vics, huntrs, ticks, map_x, map_y):
        self.map_x = map_x
        self.map_y = map_y
        self.squares = ([[Square(x,y) for x in xrange(map_y)] 
                              for y in xrange (map_x)])
        self.populate(zombs, vics, huntrs)
 

    def populate(self, zombs, vics, huntrs):
        total = zombs+vics+huntrs
        while total > 0:

            x = random.randint(0,self.map_x-1)
            y = random.randint(0,self.map_y-1)
            if self.get_square(x,y) is not None:
                if (self.get_square(x,y).get_from_square() == ""):
                    if zombs>0:
                        self.get_square(x,y).put_on_square("Zombie")
                        zombs-=1
                    elif vics>0:
                        self.get_square(x,y).put_on_square("Victim")
                        vics-=1
                    elif huntrs>0:
                        self.get_square(x,y).put_on_square("Hunter")
                        huntrs-=1
                    total-=1

    def make_move(self):
        moves = []
        # go through the square one by one
        for x in xrange(len(self.squares)):
            for y in xrange(len(self.squares[0])):
                # if the square isn't empty
                if self.get_square(x,y) is not None:
                    entity = self.get_square(x,y).get_from_square()
                    if entity != "":
                        for i in xrange(-1,2):
                            for j in xrange(-1,2):
                                #print i,j
                                try:
                                    if (self.get_square(x+i,y+j) is not None):
                                        if (self.get_square(x+i,y+j).get_from_square()=="") and (
                                                i is not 0 and j is not 0):
                                            moves+=["%d %d" % (i, j)]
                                except AttributeError:
                                    print "error"
                        
                        if len(moves)>0:
                            rand_index = random.randint(0, len(moves)-1)
                            add_x, add_y  = (moves[rand_index]).split()
                            new_x, new_y = int(add_x)+x, int(add_y)+y
                            if entity == "Hunter":
                                print "Current pos x: %d, y: %d" % (x,y)
                                print "Adding to x: %s, y: %s" % (add_x, add_y)
                                print "New pos x: %d, y: %d" % (new_x, new_y)
                                self.move_entity("Hunter", x, y, new_x, new_y)
     
    def move_entity(self, entity, old_x, old_y, new_x, new_y):
            if (self.get_square(new_x,new_y).get_from_square() == ""):
                self.get_square(new_x,new_y).put_on_square(entity)
                self.get_square(old_x,old_y).put_on_square("")


    def get_square(self, x, y):
        if (x > 0 and x < self.map_x) and (
            y > 0 and y < self.map_y):
            return self.squares[int(x)][int(y)]
        else:
            return None


    def update(self):
        self.make_move()

    def draw(self):
        #i = 0
        for x in xrange(len(self.squares)):
            for y in xrange(len(self.squares[0])):
                #print (x, y),       
                if self.get_square(x,y) is not None:    
                    if self.get_square(x,y).get_from_square() != "":
                        print self.squares[x][y].get_from_square()[0],
                    else: print '_',
                #i+=1
            print
