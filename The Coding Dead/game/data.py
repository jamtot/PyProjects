class Data(object):
    def __init__(self):
        self.zombie_stumble_units = 0
        self.victim_flee_units = 0
        self.hunter_seek_units = 0

        self.single_kills = 0
        self.double_kills = 0
        #self.zombies_killed = 0

        self.victims_bitten = 0
        self.hunters_bitten = 0
        #self.total_bitten = 0

    def print_all(self):

        zombies_killed = self.single_kills + (self.double_kills*2)
        print "Zombies have stumbled %d units." % self.zombie_stumble_units
        print "Victims have fled %d units." % self.victim_flee_units
        print "Hunters have seeked %d units." % self.hunter_seek_units
    
        print "Hunters have made %d single kills." % self.single_kills
        print "Hunters have made %d double kills." % self.double_kills
        print "There have been %d total zombies killed." % zombies_killed

        total_bitten = self.victims_bitten + self.hunters_bitten
        print "Zombies have bitten %d victims." % self.victims_bitten
        print "Zombies have bitten %d hunters." % self.hunters_bitten
        print "Zombies have bitten %d total." % total_bitten



    def add_zom_move(self):
        self.zombie_stumble_unit+=1

    def add_vic_move(self):
        self.victim_flee_unit+=1

    def add_hun_move(self):
        self.hunter_seek_unit+=1

    def add_kill(self):
        self.single_kill+=1

    def add_d_kill(self):
        self.double_kill+=1

    def add_vic_bite(self):
        self.victims_bitten+=1

    def add_hun_bite(self):
        self.hunters_bitten+=1
