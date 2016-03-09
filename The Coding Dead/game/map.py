from tile import Tile

class Map(object):
    def __init__(self, tile_size_x=20, tile_size_y=20):
        # creates an empty nested list of tiles
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y
        self.tile_list = ([[Tile(x,y) for x in xrange(tile_size_x)] 
                              for y in xrange (tile_size_y)])

    def update(self):
        for x in xrange(len(self.tile_list)):
            for y in xrange(len(self.tile_list[0])):
                print self.tile_list[x][y].printPos()

    def get_size_x(self):
        return self.tile_size_x

    def get_size_y(self):
        return self.tile_size_y
