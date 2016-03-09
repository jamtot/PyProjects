from entity import Entity

class Victim(Entity):
    # is initialised with position from base class Entity
    # and a map reference

    def flee(self):
        # a victim will not typically move
        # but will flee a zombie next to them 
        # (up, down, left, right or diagonal)
        # will move 1 square
        pass

    def update(self):
        # stay still if no zombie beside
        # flee if zombie beside
        pass
