from entity import Entity

class Zombie(Entity):
    # is initialised with position from base class Entity
    # and a map reference

    def bite(self):
        # a zombie will try to bite a non-zombie
        # up, down, left or right from it
        pass


    def move(self, potential_moves):
        x_moves, y_moves = super(Zombie,self).move(potential_moves)
        if len(x_moves) > 0 and len(y_moves) > 0: # can move at least 2 directions
            go_x = random.randint(0,9)%2 == 0
            if go_x: return ( random.randint(0, len(x_moves)-1), 0)
            else: return ( 0, random.randint(0, len(y_moves)-1))
        elif len(x_moves) > 0: return ( random.randint(0, len(x_moves)-1), 0)
        elif len(y_moves) > 0: return ( 0, random.randint(0, len(y_moves)-1))
        else: return (0,0) # no move
        
    def update(self):
        # will try move up, down, left or right only
        # will try to bite nearby non-zombie
        pass
        
        
    
    
