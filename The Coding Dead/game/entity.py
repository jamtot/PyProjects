from map import Map
import random

class Entity(object):
    def __init__(self, position):#, mapref):
        self.position = position
        #self.mapref = mapref

    def move(self, potential_moves):
        # if an entity tries to move to an occupied square,
        # stay put
        #if self.mapref(newPosition.empty()):
        x_moves = []
        y_moves = []
        for element in potential_moves:
            split = element.split()
            if (split[0] == "x"):
                x_moves.append(x_moves)
            if (split[0] == "y"):
                y_moves.append(y_moves)

        return x_moves, y_moves
        


    def update(self):
        # what to do when the game ticks
        pass
