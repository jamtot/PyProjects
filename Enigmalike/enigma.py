import random
import string

class Rotor(object):
    """ a rotor used by the Enigma class, these spin, to
        produce a different output after each letter is encoded """
    def __init__(self, teeth, position, charset):
        self.teeth = teeth
        self.position = position
        self.chars = charset

    def spin(self):
        """ spins the rotor, returns true if the wheel has been
            reset to 0 (not 0 == True) """
        self.position = (self.position + 1) % self.teeth
        return not self.position

    def unspin(self):
        """ turns the rotor back 1 notch, returning True
            if the wheel has been set back from 0 """
        self.position = self.position - 1
        if self.position < 0: 
            self.position = self.teeth-1
            return True
        return False

    def getindex(self, ch):
        """ gets the index of character ch from the rotors
            characterset """
        return self.chars.index(ch)

    def getcharfromindex(self, index):
        """ returns the character residing at the index provided.
            there are measures to stop it going out of bounds """
        if index < 0:
            index = (self.lenchars()-(abs(index)))
        index = index%self.lenchars()
        return self.chars[index]

    def setpos(self, newpos):
        self.position = newpos%self.teeth

    def getpos(self):
        return self.position

    def lenchars(self):
        return len(self.chars)


    
class Enigma(object):
    
    def __init__(self, rseed = 12345, nrotors = 3, nteeth = 26, positions = [0,0,0], usespecialchars=False, charset = ' '+(
    "".join(string.printable.split()))):
        # can add \n, \t, \r etc. to the charset, but results in random uses of the characters throughout
        if (usespecialchars): charset="\n\t\r\b"+charset
        self.charset = charset
        random.seed(rseed)
        self.rotors = [self.newrotor(nteeth, positions[i], charset) for i in xrange(nrotors)]
        
    def newrotor(self, teeth, positions, charset):
        """ returns a new rotor using a random integer to split the 
            charset string and re-attach them with the end and start
            joinging, so that indices from one rotor to another don't
            match """
        index = random.randint(0,len(charset)-1)
        return Rotor(teeth, positions, charset[index:]+charset[:index])

    def encodech(self, ch):
        """ spins the rotor/s before using each rotor, then converts
            the original starting letter into an index, which it
            uses added to a number generated off the wheel positions
            to grab a letter from the next rotor, and so on"""
        try:
            index = 0
            for i in xrange(self.getrotsiz()-1):
                self.progress()
                index = self.rotors[i].getindex(ch)+self.sumrotpos()
                ch = self.rotors[i+1].getcharfromindex(index)
        except ValueError:
            # character not in charset
            self.regress()
            pass 
        return ch
        
    def decodech(self, ch):
        """ reverses the encodech() process, using the letter index
            minus the number generated off the wheel positions to get
            the previous rotors char, and winds back the rotor/s after
            each step """
        try:
            index = 0
            for i in xrange(self.getrotsiz()-1, 0, -1):
                index = self.rotors[i].getindex(ch)-self.sumrotpos()
                ch = self.rotors[i-1].getcharfromindex(index)
                self.regress()
        except ValueError:
            # character not in charset
            pass
        return ch
    
    def encode(self, string):
        """ goes through the string, sending each 
            character to be mixed up """
        string = list(string)
        for i in xrange(len(string)):
            string[i] = self.encodech(string[i])
        return "".join(string)

    def decode(self, string):
        """ goes through the string, sending each 
            character to be unmixed up """
        string = list(string)
        for i in xrange(len(string)-1, -1, -1):
            string[i] = self.decodech(string[i])
        return "".join(string)

    def progress(self):
        """turns the first rotor on notch, and the next after
            each full rotation, and the next, etc.""" 
        if self.rotors[0].spin():
            if self.rotors[1].spin():
                self.rotors[2].spin()

    def regress(self):
        """turns the first rotor back a notch, and the next, etc.
            after each full rotation back"""
        if self.rotors[0].unspin():
            if self.rotors[1].unspin():
                self.rotors[2].unspin()
            
    def getrotsiz(self):
        return len(self.rotors)

    def sumrotpos(self):
        return (sum([r.getpos() for r in self.rotors]))**2

    def getrotsettings(self):
        return [r.getpos() for r in self.rotors]
        
    def setrotsettings(self,positions):
        if len(positions) == self.getrotsiz():
            for i in xrange(self.getrotsiz()):
                self.rotors[i].setpos(positions[i])
  


if __name__=="__main__":
    # not converting \n\r\t and \b
    cypher = Enigma(4424,3,26,[0,0,0],False)

    # converting \n\r\t and \b too
    scypher = Enigma(4424,3,26,[0,0,0],True)

    s = """\tHey,\n\t\tHow are  \byou?
\t\t\t\t\rI'm good."""
    print s

    print "Encoding without special chars."
    e = cypher.encode(s)
    print e
    print "Decoding."
    d = cypher.decode(e)
    print d
    
    print "----------------"
    print "Encoding with special chars."
    se = scypher.encode(s)
    print se
    print "Decoding."
    sd = scypher.decode(se)
    print sd

