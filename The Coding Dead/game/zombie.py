from entity import Entity

class Zombie(Entity):
    # is initialised with position from base class Entity
    # and a map reference

    def bite(self):
        # a zombie will try to bite a non-zombie
        # up, down, left or right from it
        pass

    def update(self):
        # will try move up, down, left or right only
        # will try to bite nearby non-zombie
        pass
        
        
    
    
