input = """chat.freenode.net:6667
ggnore
ggnore
ggnore
#rdpPONG,#gg,#botters-test,#reddit-dailyprogrammer
Hello, world!"""

def from_file(filename):
    """takes a list of words from a file"""
    with open(filename) as rawfile:
        return rawfile.read().splitlines()

lols=from_file("lol.txt")
chefs=from_file("chef.txt")

import socket
import threading

class Connection(object):
    def __init__(self, server):
        self.server, self.port = server.split(":")
        self.socky = socket.socket()
        self.received = ""

    def connect(self):
        self.socky.connect((self.server, int(self.port)))
        print "Connected."

    def close(self):
        self.socky.close()

    def send(self, msg):
        self.socky.send(msg+"\r\n")

    def recv(self):
        if "\r\n" not in self.received:
            self.received += self.socky.recv(512)
        line, self.received = self.received.split("\r\n", 1)
        # split line to check input type
        line = line.split()
        # if the first word is ping, pong
        if line[0] == "PING":
            print " ".join(line)
            pong = "PONG %s"%line[1]
            self.send(pong)
        return line

class Bot(object):
    def __init__(self, server, nickname, username, realname, channels, message):
        self.connection = Connection(server)
        self.nickname = nickname
        self.username = username
        self.realname = realname
        self.channels = channels
        self.message = message
        self.server_name = "*"
        self.user_mode = 0
        self.current_channel = ''
        self.running = False
        self.line=[]
        self.setup()


    def setup(self):
        self.running = True
        self.connection.connect()
        nickmsg = "NICK %s" % self.nickname
        usermsg = "USER %s %d %s :%s" % (self.username, self.user_mode,
                                       self.server_name, self.realname)
        self.send(nickmsg)
        self.send(usermsg)
        print "Initial details sent."

    def send(self, msg):
        self.connection.send(msg)

    def outbound(self):
        while self.running:
            pass

    def inbound(self):
        while self.running:
            self.line = self.connection.recv()
            print " ".join(self.line)
    
            # when the MOTD has shown, join channels
            if self.line[1] == "376":
                joinmsg="JOIN %s"%channels
                self.send(joinmsg)
            elif ":GTFO" in self.line[3:] and "BOTYO" in self.line[4:]:
                chefmsg = "PRIVMSG %s :GTFOing"%(self.line[2])
                self.send(chefmsg) 
                self.send("QUIT") 
                self.running = False
                self.connection.close()

if __name__=="__main__":
    server, nickname, username, realname, channels, message  = input.splitlines()
    myBot = Bot(server, nickname, username, realname, channels, message)

    in_thread = threading.Thread(target = myBot.inbound)
    out_thread = threading.Thread(target = myBot.outbound)
    in_thread.start()
    out_thread.start()
    exit(1)
