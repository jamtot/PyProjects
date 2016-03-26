import sys
import datetime
import readline
import random

#math functions
#-------------------------------------------------------------------
# using an iterative factorial so there's no deptherror
def fac(n):
    if n < 0:
        n=n*-1
    for i in xrange(n-1, 1, -1):
        n*=i
    return n

# this will only go 998 deep, usually 999 deep
def recfac(n):
    if n < 0:
        n=n*-1
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def recfib(num):
    if num<=1:
        return num
    else:
        return rec_fib(num-1)+rec_fib(num-2)

def fib(num):
    if num>1: 
        a=0
        b=1
        count=1
        #print b
        while count<num:    
            b,a=a,a+b
            count+=1
        return a
    else: return "Nice try, bub."

def sum(nums):
    nums = nums.split(" ")
    try:
        total = sum(map(int, nums))
        return "PRIVMSG %s :%s: The sum is: %d"%(to, sender, total)
    except ValueError:
        return "PRIVMSG %s :%s: ValueError"%(to, sender)

def diff(nums):
    nums = nums.split(" ")
    try:
        total = reduce(lambda x,y: x-y, map(int,nums))
        return "PRIVMSG %s :%s: The diff is: %d"%(to, sender, total)

    except ValueError:
        return "PRIVMSG %s :%s: ValueError"%(to, sender)

def mult(nums):
    nums = nums.split(" ")
    try:
        total = reduce(lambda x,y: x*y, map(int,nums))
        return "PRIVMSG %s :%s: The mult is: %d"%(to, sender, total)
    except ValueError:
        return "PRIVMSG %s :%s: ValueError"%(to, sender)


def div(nums):
    nums = nums.split(" ")
    try:
        total = reduce(lambda x,y: x/y, map(int,nums))
        return "PRIVMSG %s :%s: The div is: %d"%(to, sender, total)
    except ValueError:
        return "PRIVMSG %s :%s: ValueError"%(to, sender)

    except ZeroDivisionError:
        return "PRIVMSG %s :%s: SUCK IT!"%(to, sender)


#-------------------------------------------------------------------

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
m8ball=from_file("8ball.txt")

phrases=from_file("phrases.txt")
phrdict={}
phrlist=[]

for phrase in phrases:
    p = phrase.split("-")
    phrlist+=[p[0]]
    phrdict[p[0]] = p[1]

def chef_scan(msg):
    if "chef" in msg:
        return chefs[random.randint(0,len(chefs)-1)]
    return None

def lol_scan(msg):
    if any(lol in msg for lol in lols):
        return lols[random.randint(0,len(lols)-1)]
    return None

def m8ball_scan(msg, nickname):
    if "?" in msg and nickname.lower() in msg:
        return m8ball[random.randint(0,len(m8ball)-1)]
    return None

def phrase_scan(msg):
    if any(phr in msg for phr in phrlist):
        for phr in phrlist:
            if phr in msg:
                return phrdict[phr]
    return None
#-------------------------------------------------------------------
