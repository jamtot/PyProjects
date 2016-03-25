input = """chat.freenode.net:6667
gg-no-re
gg-no-re
gg-no-re
#rdpPONG,#gg
Hello, world!"""



import socket
import threading
import datetime
import readline
import sys

# helfpul functions
#-------------------------------------------------------------------
# returns a list of the lines from a file
def from_file(filename):
    """takes a list of words from a file"""
    with open(filename) as rawfile:
        return rawfile.read().splitlines()

# returns the current time in a nicely formatted form
def get_timestamp():
    now = datetime.datetime.now()
    return "[%02d:%02d:%02d]" % (now.hour, now.minute, now.second)

# saves the current line, prints the new line, then puts the current
# line back (good for stopping your text being corrupted)
def interrupt_text(new_stuff):
    sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
    print new_stuff
    sys.stdout.write(readline.get_line_buffer())
    sys.stdout.flush()

def msg_formatter(room, sender, msg):
    return ("%s %s <%s> %s"% (get_timestamp(),room,sender,msg))

def line_overwrite():
    print "\033[A                             \033[A" 
#-------------------------------------------------------------------

# silly things
#-------------------------------------------------------------------
lols=from_file("lol.txt")
chefs=from_file("chef.txt")
#-------------------------------------------------------------------

# connection class
#-------------------------------------------------------------------
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
        chkmsg = line.split()

        # if the first word is ping, pong
        if chkmsg[0] == "PING":
            #print " ".join(line)
            pong = "PONG %s"%chkmsg[1]
            self.send(pong)
        # if it's a message in, print it
        elif chkmsg[1] == "PRIVMSG":
            sender = chkmsg[0].split("!")[0][1:]
            msg = " ".join(chkmsg[3:])[1:]# loses the ':' at the start
            interrupt_text(msg_formatter(chkmsg[2], sender, msg))
        else: print line

        return line
#-------------------------------------------------------------------

# bot class
#-------------------------------------------------------------------
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
        self.current_channel = '#gg'


    def setup(self):
        self.running = True
        self.connection.connect()
        nickmsg = "NICK %s" % self.nickname
        usermsg = "USER %s %d %s :%s" % (self.username, self.user_mode,
                                       self.server_name, self.realname)
        self.send(nickmsg)
        self.send(usermsg)
        print "Initial details sent."

    def send(self, msg, printit=True):
        if printit: print msg
        self.connection.send(msg)

    def outbound(self):
        while self.running:
            input_ = raw_input()

            #if there's nothin input, skip to next loop
            if not input_:
                continue
            else:
                self.get_user_input(input_)
        return None

    def inbound(self):
        while self.running:
            self.line = self.connection.recv()
            #print self.line

            self.line = self.line.split()
    
            # when the MOTD has shown, join channels
            if self.line[1] == "376":
                joinmsg="JOIN %s"%self.channels
                self.channels = self.channels.split(",")
                
                self.send(joinmsg)

            elif ":gg" in self.line[3:]:
                chefmsg = "PRIVMSG %s :no re"%(self.line[2])
                self.send(chefmsg) 
                self.send("QUIT") 
                self.running = False
                self.connection.close()
                #exit(1)
        return None

    def get_user_input(self, t_input):
        
        # closing the client
        if "/quit" in t_input:
            # kind of errors on the closing (due to second thread)
            msg = "PRIVMSG %s :%s OUT!"%(self.current_channel,self.nickname)
            self.send(msg)
            self.send("QUIT")
            self.running = False
            self.connection.close()  
            #exit(1)

        # switch channel
        elif "/ch" in t_input:
            t_input = t_input.split("/ch")
            if t_input[1] in self.channels:
                print "Switching to %s" % t_input[1]
                self.current_channel = t_input[1]
            else:
                print "Not in %s, joining." % t_input[1]
                self.current_channel=t_input[1]
                joinmsg="JOIN %s"%self.current_channel
                self.channels.append(t_input[1])
                self.send(joinmsg)

        # change the nickname
        elif "/nick" in t_input:
            # no handling of taken nicknames
            t_input = t_input.split("/nick")
            if len(t_input[1])>0:
                print "changing nick to %s" % t_input[1]
                self.nick = t_input[1]
                self.send("NICK %s"% t_input[1])

        # no commands, just output the input as a message in chat
        else:
            if self.current_channel != '':
                # used to remove the input and write over where it was
                line_overwrite()
                print msg_formatter(self.current_channel,self.nickname,t_input)
                #print "%s %s <%s> %s"% (get_timestamp(),self.current_channel,self.nickname,t_input)
                msg = "PRIVMSG %s :%s"%(self.current_channel,t_input)
                self.send(msg, False) 
#------------------------------------------------------------------

if __name__=="__main__":
    server, nickname, username, realname, channels, message  = input.splitlines()
    myBot = Bot(server, nickname, username, realname, channels, message)
    
    in_thread = threading.Thread(target = myBot.inbound)
    out_thread = threading.Thread(target = myBot.outbound)
    in_thread.start()
    out_thread.start()
