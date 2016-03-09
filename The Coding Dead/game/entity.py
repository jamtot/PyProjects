from map import Map

class Entity(object):
    def __init__(self, position, mapref):
        self.position = position
        self.mapref = mapref

    def move(self, newPosition):
        # if an entity tries to move to an occupied square,
        # stay put
        if self.mapref(newPosition.empty()):
            self.position = newPosition

    def update(self):
        # what to do when the game ticks
        pass
