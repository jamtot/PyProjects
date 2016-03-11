import random
from map import Map

class Game(object):
    def __init__(self, x, y, z, t, map_x=20, map_y=20):
        """
        x - zombies to randomly spawn
        y - victims to randomly spawn
        z - hunters to randomly spawn
        t - ticks the game will simulate
        map_x - amount of rows in the map
        map_y - amount of columns in the map
        """
        self.map = Map(map_x, map_y)
        self.map_x = map_x
        self.map_y = map_y
        self.x = x
        self.y = y
        self.z = z
        self.total_entities = x+y+z
        self.t = t

    def populate(self):
        i,j,k,l = 0,0,0,0
        while i < (self.total_entities):
            # generate random tile location
            x = random.randint(0,self.map_x-1)
            y = random.randint(0,self.map_y-1)
            #print "%d,%d" %(x,y)
            # check for occupation
            if (self.map.get_tile(x,y).is_occupied()):
                # is already occupied
                pass
            else: # not occupid
                # add entity
                if j < self.x: # add zombie
                    self.map.get_tile(x,y).occupy("Zombie")                    
                    j+=1
                elif k < self.y: # add victim
                    self.map.get_tile(x,y).occupy("Victim") 
                    k+=1
                elif l < self.z: # add hunter
                    self.map.get_tile(x,y).occupy("Hunter")
                    l+=1       
                #increment i
                i+=1

    def update(self):
        self.map.update()

    def simulate(self):
        for i in xrange(self.t):
            self.update()

    def get_map(self):
        return self.map

if __name__ == "__main__":
    print "Creating game."
    myGame = Game(1,0,0,1,2,2)
    print "Populating map."
    myGame.populate()
    print "Running simulation."
    myGame.simulate()
        
