import random

class Game(object):
    def __init__(self, maxgames):
        self.bestof=self.getgames(maxgames)
        self.p1wins=0
        self.compwins=0
        self.gdict={1:"Rock",2:"Paper",3:"Scissors"}

    def getgames(self, maxgs):
        g2p=-1
        print
        while g2p < 0 or g2p > maxgs:
            print "How many games (best-of): "
            choice = raw_input("> ")
            if choice.isdigit():
                g2p = int(choice)
            if g2p > maxgs:
                print "Too high, setting to %d"%maxgs
                g2p=maxgs
            elif g2p < 0:
                g2p=-1
                print "Too low, try again."
        print
        return g2p

    def play(self):
        print "Game on! Best of %d games."%self.bestof
        print
        print "r or 1 for rock"
        print "p or 2 for paper"
        print "s or 3 for scissors"
        print
        r=["1","r","R"]
        p=["2","p","P"]
        s=["3","s","S"]
        acceptable=[x for ilist in [r,p,s] for x in ilist]

        while self.p1wins+self.compwins < self.bestof:
            choice = raw_input("GO! > ")
            if choice in acceptable:
                if choice in r:
                    self.playhand(1)
                elif choice in p:
                    self.playhand(2)
                elif choice in s:
                    self.playhand(3)
            else: print "Enter r, p or s | 1, 2 or 3."
        if (self.p1wins>self.compwins):
            print "Congratulations, you won the game!"
        elif (self.p1wins==self.compwins):
            print "You drew! This is why best-ofs aren't even."
        else:
            print "You are dead."
        print
        exit(1)

    def playhand(self, p_hand):
        c_hand=random.randint(1,3)
        print
        print "You: %s CPU: %s"%(self.gdict[p_hand],self.gdict[c_hand])
        if (p_hand==1 and c_hand==3) or (p_hand==2 and c_hand==1) or (
                        p_hand==3 and c_hand==2):
            print "%s beats %s"%(self.gdict[p_hand],self.gdict[c_hand])
            print "Your round!"
            self.p1wins+=1
        elif p_hand==c_hand:
            print "Samesies! Go again."
        else:
            print "%s beats %s"%(self.gdict[c_hand],self.gdict[p_hand])
            print "CPUs round!"
            self.compwins+=1
        print "%d - %d" % (self.p1wins, self.compwins)
        print
                
                

if __name__ == "__main__":
    grps=Game(9)
    grps.play()
        
    
