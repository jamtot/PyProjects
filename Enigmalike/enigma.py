import re
import random
import string

class Rotor(object):
    def __init__(self, charset, teeth=26, position = 0):
        self.teeth = teeth
        self.position = position
        self.chars = charset

    def spin(self):
        self.position = (self.position + 1) % self.teeth
        return not self.position

    def unspin(self):
        self.position = self.position - 1
        if self.position < 0: 
            self.position = self.teeth-1
            return True
        return False

    def setpos(self, newpos):
        self.position = newpos%self.teeth

    def getpos(self):
        return self.position

    def getchars(self):
        print self.chars

    def lenchars(self):
        return len(self.chars)

    def getindex(self, ch):
        return self.chars.index(ch)

    def getcharfromindex(self, index):
        if index < 0:
            index = (self.lenchars()-(abs(index)))
        index = index%self.lenchars()
        return self.chars[index]
    
class Enigma(object):

    def __init__(self, rseed = 12345, nrotors = 3, charset = ' '+("".join(string.printable.split()))):
        self.charset = charset
        random.seed(rseed)
        self.rotors = [self.newrotor(charset) for i in xrange(nrotors)]

        
    def newrotor(self, charset):
        index = random.randint(0,len(charset)-1)
        return Rotor(charset[index:]+charset[:index])

    def progress(self):
        if self.rotors[0].spin():
            if self.rotors[1].spin():
                self.rotors[2].spin()

    def regress(self):
        if self.rotors[0].unspin():
            if self.rotors[1].unspin():
                self.rotors[2].unspin()

    def printpos(self):
        for r in self.rotors:
            print r.getpos(),
        print

    def printchars(self):
        for r in self.rotors:
            print r.getchars(),
        print
            
    def getrotsiz(self):
        return len(self.rotors)

    def sumrotpos(self):
        return (sum([r.getpos() for r in self.rotors]))**2

    def encode(self, ch):
        try:
            
            index = 0
            for i in xrange(self.getrotsiz()-1):
                self.progress()
                index = self.rotors[i].getindex(ch)+self.sumrotpos()
                ch = self.rotors[i+1].getcharfromindex(index)
        except ValueError:
            pass # character not in charset


        return ch
        

    def decode(self, ch):
        try:
            index = 0
            for i in xrange(self.getrotsiz()-1, 0, -1):
                index = self.rotors[i].getindex(ch)-self.sumrotpos()
                ch = self.rotors[i-1].getcharfromindex(index)
                self.regress()
        except ValueError:
            pass # character not in charset
        return ch
    

    def encodestring(self, string):
        string = list(string)
        for i in xrange(len(string)):
            string[i] = self.encode(string[i])
        return "".join(string)

    def decodestring(self, string):
        string = list(string)
        for i in xrange(len(string)-1, -1, -1):
            string[i] = self.decode(string[i])
        return "".join(string)

    def getrotsettings(self):
        return [r.getpos() for r in self.rotors]
        
    def setrotsettings(self,positions):
        if len(positions) == self.getrotsiz():
            for i in xrange(self.getrotsiz()):
                self.rotors[i].setpos(positions[i])
  


if __name__=="__main__":
    enig = Enigma()
    #enig.printchars()
    print enig.getrotsettings()
    string1 = "Hello, my name is Jonathan Morris."
    print string1
    string1 = enig.encodestring(string1)
    nstring1 = str(string1)
    s1settings = enig.getrotsettings()
    print string1

    string2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    print string2
    string2 = enig.encodestring(string2)
    print "This encodes to '%s'"%string2

    print enig.getrotsettings()
    string1 = enig.decodestring(string1)
    print string1

    string2 = enig.decodestring(string2)
    print "This decodes to '%s'"%string2


    enig.setrotsettings(s1settings)
    print nstring1  
    nstring1 = enig.decodestring(nstring1)
    print nstring1
    print enig.getrotsettings()

    




    #print ' '+("".join(string.printable.split()))
