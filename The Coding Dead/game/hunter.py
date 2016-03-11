from entity import Entity

class Hunter(Entity):
    # is initialised with position from base class Entity
    # and a map reference   
 
    def destroy_zombie(self):
        # use position to check nearby tiles for zombies
        # check in every direction
        # kill up to 2 zombies
        pass

    def move(self, potential_moves):
        x_moves, y_moves = super(Hunter,self).move(potential_moves)

    def update(self):
        # can move 1 square in any direction to find zombie to kill
        # can slay up to two zombies after a move
        pass
