from tile import Tile

class Map(object):
    def __init__(self, tile_size_x=20, tile_size_y=20):
        # creates an empty nested list of tiles
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y
        self.tile_list = ([[Tile(x,y) for x in xrange(tile_size_y)] 
                              for y in xrange (tile_size_x)])

    def update(self):
        for x in xrange(len(self.tile_list)):
            for y in xrange(len(self.tile_list[0])):
                #print self.tile_list[x][y].update()
                pass

    def get_tile(self, x, y):
        return self.tile_list[x][y]

    def get_size_x(self):
        return self.tile_size_x

    def get_size_y(self):
        return self.tile_size_y

    def get_list(self):
        return self.tile_list

    def get_moves(self):
        occupied_tiles = []
        potential_moves = []
        for x in xrange(len(self.tile_list)):
            for y in xrange(len(self.tile_list[0])):
                if self.tile_list[x][y].is_occupied():
                    occupied_tiles.append(self.tile_list[x][y])

        for tile in occupied_tiles:
            position = tile.position
            if position[0]-1 > 0:# can move back one (x)
                potential_moves.append("x -1")
            if position[0]+1<self.tile_size_x:# can move forward one (x)
                potential_moves.append("x 1")
            if position[1]-1 > 0:# can move back one (y)
                potential_moves.append("y -1")
            if position[1]+1<self.tile_size_x:# can move forward one (y)
                potential_moves.append("y 1")

        return occupied_tiles, potential_moves

    def make_moves(self):
        occupied_tiles, potential_moves = self.get_moves()
        for tile in occupied_tiles:
            tile.get_entity().move(potential_moves)

    def draw(self):
        for x in xrange(len(self.tile_list)):
            for y in xrange(len(self.tile_list[0])):
                if self.tile_list[x][y].is_occupied():
                    print self.tile_list[x][y].occupier[0],
                else: print '_',
            print
