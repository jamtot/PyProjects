from map import Map

class Game(object):
    def __init__(self, zombs, vics, huntrs, ticks, map_x=20, map_y=20):
        self.map = Map(zombs, vics, huntrs, ticks, map_x, map_y)
        self.ticks = ticks

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()

    def simulate(self):
        for i in xrange(self.ticks):
            self.update()
            self.draw()

myGame = Game(1, 1, 1, 5, 5, 4)
myGame.draw()

myGame.simulate()
