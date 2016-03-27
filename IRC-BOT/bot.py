input = """chat.freenode.net:6667
knook
knook
knook
#rdpPONG,#gg
Hi, I'm a bot."""

#,#reddit-dailyprogrammer,#rdp,#botters-test

import socket
import threading
from funcs import *

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
        else: interrupt_text(line)

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


    #INBOUND TRAFFIC
    #----------------------------
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
            else:
                try:
                    self.word_scan(self.line[2], " ".join(self.line[3:]).lower())   
                except IndexError:
                    pass

            if self.line[1] == "PRIVMSG" and self.nickname + ":" in self.line[3]:
                sender = self.line[0].split("!")[0][1:]
                if self.line[2] in self.channels or self.line[2] in self.nickname:
                    to = self.line[2] if self.line[2] in self.channels else sender
                    self.messaged(to, sender, " ".join(self.line[4:]))

            elif self.line[1] == "PRIVMSG" and self.nickname in self.line:
                sender = self.line[0].split("!")[0][1:]
                if self.line[2] in self.channels or self.line[2] in self.nickname:
                    to = self.line[2] if self.line[2] in self.channels else sender
                    self.mentioned(to, sender, " ".join(self.line[3:]))

            elif ":gg" in self.line[3:]:
                chefmsg = "PRIVMSG %s :no re"%(self.line[2])
                self.send(chefmsg) 
                self.send("QUIT") 
                self.running = False
                self.connection.close()
                #exit(1)

            elif ":eval" in self.line[3:]:
                evalmsg=''
                try:
                    evalmsg=str(eval(" ".join(self.line[4:])))

                except SyntaxError:
                    evalmsg="SyntaxError"
                except ZeroDivisionError:
                    evalmsg="Bleep Bloop SUCK IT"
                except NameError:
                    evalmsg="It's like you are trying to break me!"
                

                evalmsg = "PRIVMSG %s :%s"%(self.line[2],evalmsg)
                self.send(evalmsg) 
        return None
    #/INBOUND TRAFFIC
    #----------------------------

    #OUTBOUND TRAFFIC
    #----------------------------
    def outbound(self):
        while self.running:
            input_ = raw_input()

            #if there's nothin input, skip to next loop
            if not input_:
                continue
            else:
                self.get_user_input(input_)
        return None
    #--------------------------------------------
    def get_user_input(self, t_input):
        
        # closing the client
        if t_input.startswith("/quit"):
            # kind of errors on the closing (due to second thread)
            for chan in self.channels:
                msg = "PRIVMSG %s :%s OUT!"%(chan,self.nickname.upper())
                self.send(msg)
            self.send("QUIT")
            self.running = False
            self.connection.close()  
            #exit(1)

        # switch channel
        elif t_input.startswith("/ch "):
            t_input = t_input.split("/ch ")
            if t_input[1] in self.channels:
                print "Switching to %s" % t_input[1]
                self.current_channel = t_input[1]
            else:
                print "Not in %s, joining." % t_input[1]
                if t_input[1].startswith("#"):
                    self.current_channel=t_input[1]
                    joinmsg="JOIN %s"%self.current_channel
                    self.channels.append(t_input[1])
                    self.send(joinmsg)
                else:
                    print "You forgot the #"

        elif t_input.startswith("/cur"):
            for chan in self.channels:
                interrupt_text(chan),
            

        elif "/join " in t_input:
            t_input = t_input.split("/join ")
            self.current_channel = t_input[1]
            print "Joining %s"% self.current_channel
            joinmsg="JOIN %s"%self.current_channel
            if self.current_channel not in self.channels:
                self.channels.append(self.current_channel)
            self.send(joinmsg)

        # change the nickname
        elif t_input.startswith("/nick "):
            # no handling of taken nicknames
            t_input = t_input.split("/nick ")
            if len(t_input[1])>0:
                print "changing nick to %s" % t_input[1]
                self.nickname = t_input[1]
                self.send("NICK %s"% t_input[1])

        # write to all channels you are in
        elif t_input.startswith("/all "):
            if len(self.channels) > 0:
                t_input = t_input.split("/all ")
                #t_input = "".join(t_input[1:])
                line_overwrite()
                for chan in self.channels:
                    self.sndmsg(chan, t_input[1])

        elif t_input.startswith("/part "):
            t_input = t_input.split("/part ")
            line_overwrite()
            self.send("PART %s"%(t_input[1]))
            if t_input[1] in self.channels:
                self.channels.remove(t_input[1])
                if t_input[1] == self.current_channel:
                    if len(self.channels)>0:
                        self.current_channel = self.channels[0]
                    else:
                        self.current_channel=''

        # write to all channels you are in
        elif t_input.startswith("/me "):
            t_input = t_input.split("/me ")
            line_overwrite()
            self.send("PRIVMSG %s :\x01ACTION %s\x01"%(
                self.current_channel,t_input[1]))
        
        elif t_input.startswith("/msg "):
            try:
                t_input = t_input.split("/msg ")[1]
                print t_input
                t_input = t_input.split()
                if len(t_input)>1:
                    self.sndmsg(t_input[0], " ".join(t_input[1:]))
            except AttributeError:
                print "%s<- , %s<- " % (t_input[0], " ".join(t_input[1:]))
                print "whaddaya a meatball?"
                

        # no commands, just output the input as a message in chat
        else:
            if self.current_channel != '':
                # used to remove the input and write over where it was
                line_overwrite()
                self.sndmsg(self.current_channel,t_input) 
    #/OUTBOUND TRAFFIC
    #----------------------------

    def send(self, msg, printit=True):
        if printit: print msg
        self.connection.send(msg)

    def sndmsg(self,channel,msg, self_interupting=False):
        if not self_interupting:
            print msg_formatter(channel,self.nickname,msg)
            self.send("PRIVMSG %s :%s"%(channel,msg), False)
        else:
            interrupt_text(msg_formatter(channel,self.nickname,msg))
            self.send("PRIVMSG %s :%s"%(channel,msg), False)

    def messaged(self, mRoom, mFrom, mMsg):
        print "DIRECT %s <%s> %s"%(
                    mRoom, mFrom, mMsg)
    def mentioned(self, mRoom, mFrom, msg):
        print "MENTIONED %s <%s> %s" % (mRoom, mFrom, msg) 

    def imessaged(self, line):
        print "~~"+" ".join(line)+"~~"

    # 
    def word_scan(self, room, text):     
        if chef_scan(text):
            self.sndmsg(room,chef_scan(text),True)
        elif lol_scan(text):
            self.sndmsg(room,lol_scan(text),True)
        elif m8ball_scan(text, self.nickname):
            self.sndmsg(room,m8ball_scan(text, self.nickname),True)
        elif phrase_scan(text):
            self.sndmsg(room,phrase_scan(text),True)
#------------------------------------------------------------------

if __name__=="__main__":
    server, nickname, username, realname, channels, message  = input.splitlines()
    myBot = Bot(server, nickname, username, realname, channels, message)
    
    in_thread = threading.Thread(target = myBot.inbound)
    out_thread = threading.Thread(target = myBot.outbound)
    in_thread.start()
    out_thread.start()
