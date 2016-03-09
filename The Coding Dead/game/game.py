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
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def populate(entity, amount):
        # fill amount of tiles with entity
        # use random numbers to place,
        # try again if space occupied
        pass

    def update(self):
        self.map.update()

    def simulate(self):
        for i in xrange(self.t):
            self.update()

if __name__ == "__main__":
    print "Creating game."
    myGame = Game(30,50,33,5,12,24)
    print "Running simulation."
    myGame.simulate()
        
