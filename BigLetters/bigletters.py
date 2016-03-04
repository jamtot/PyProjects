A =     [' *** ',
         '*   *',
         '*****',
         '*   *',
         '*   *']
B =     ['**** ','*   *','**** ','*   *','**** ']
C =     [' *** ','*   *','*    ','*   *',' *** ']
D =     ['**** ','*   *','*   *','*   *','**** ']
E =     ['*****','*    ','***  ','*    ','*****']
F =     ['*****','*    ','***  ','*    ','*    ']
G =     [' *** ','*    ','*  **','*   *',' *** ']
H =     ['*   *','*   *','*****','*   *','*   *']
I =     ['*****','  *  ','  *  ','  *  ','*****']
J =     ['    *','    *','    *','*   *',' *** ']
K =     ['*   *','*  * ','***  ','*  * ','*   *']
L =     ['*    ','*    ','*    ','*    ','*****'] 
M =     ['*   *','** **','* * *','*   *','*   *'] 
N =     ['*   *','**  *','* * *','*  **','*   *'] 
O =     [' *** ','*   *','*   *','*   *',' *** '] 
P =     ['**** ','*   *','**** ','*    ','*    '] 
Q =     [' *** ','*   *','*   *','*  **',' ****'] 
R =     ['**** ','*   *','**** ','* *  ','*  **'] 
S =     [' *** ','*    ',' *** ','    *','**** '] 
T =     ['*****','  *  ','  *  ','  *  ','  *  '] 
U =     ['*   *','*   *','*   *','*   *',' *** '] 
V =     ['*   *','*   *','*   *',' * * ','  *  '] 
W =     ['*   *','*   *','* * *','* * *',' * * '] 
X =     ['*   *',' * * ','  *  ',' * * ','*   *'] 
Y =     ['*   *',' * * ','  *  ','  *  ','  *  '] 
Z =     ['*****','   * ','  *  ',' *   ','*****'] 
SPACE=  ['*****','*****','*****','*****','*****']
COMMA=  ['     ','     ','     ',' **  ','***  ']
STOP=   ['     ','     ',' *** ',' *** ',' *** ']
EQUALS= ['     ','*****','     ','*****','     ']
PLUS=   ['  *  ','  *  ','*****','  *  ','  *  ']
MINUS=  ['     ','     ','*****','     ','     ']
ONE=    ['  *  ',' **  ','* *  ','  *  ','*****']
TWO=    [' *** ','*   *','   * ',' **  ','*****']
THREE=  [' *** ','*   *','  ** ','*   *',' *** ']
FOUR=   ['*   *','*   *','*****','    *','    *']
FIVE=   ['*****','*    ','**** ','    *','**** ']
SIX=    ['  *  ',' *   ','**** ','*   *',' *** ']
SEVEN=  ['*****','   * ','  *  ','  *  ','  *  ']
EIGHT=  [' *** ','*   *',' *** ','*   *',' *** ']
NINE=   [' ****','*   *',' ****','   * ','  *  ']
ZERO=   [' *** ','*  **','* * *','**  *',' *** ']
QUEST=  [' *** ','*   *','   * ','  *  ','  *  ']
EXCLAM= [' *** ',' *** ',' *** ','     ',' *** ']
BACKSL= ['*    ','**   ',' **  ','  ** ','   **']
FORSL=  ['    *','   **','  ** ',' **  ','**   ']
HASH=   [' * * ','*****',' * * ','*****',' * * ']
AT=     [' *** ','*   *','*  **','*    ',' *** ']
COLON=  ['     ',' **  ','     ',' **  ','     ']
SEMIC=  ['     ',' **  ','     ',' **  ','  *  ']
DQUOT=  ['** **','** **','     ','     ','     ']
SQUOT=  ['  ** ','  ** ','     ','     ','     ']  


symbols = {'A':A, 'B':B, 'C':C, 'D':D, 'E':E, 'F':F, 'G':G, 'H':H, 
'I':I, 'J':J, 'K':K, 'L':L, 'M':M, 'N':N, 'O':O, 'P':P, 'Q':Q, 'R':R,
'S':S, 'T':T, 'U':U, 'V':V, 'W':W, 'X':X, 'Y':Y, 'Z':Z, ' ':SPACE,
',':COMMA, '.':STOP, '=':EQUALS, '+':PLUS, '-':MINUS, '1':ONE, '2':TWO, 
'3':THREE,'4':FOUR, '5':FIVE, '6':SIX, '7':SEVEN, '8':EIGHT, '9':NINE, 
'0':ZERO, '?':QUEST, '!':EXCLAM, '\\':BACKSL, '/':FORSL, '#':HASH,
'@':AT, ':':COLON, ';':SEMIC, '"':DQUOT, '\'':SQUOT}

# added some error detection
def makeBigLetters(input):
    capInput = list(input.upper())
    print '\n'
    for i in xrange(5):
        for j in xrange(len(capInput)):
            try:
                symbols[capInput[j]]
            except KeyError:
                capInput[j] = ' '
            line = symbols[capInput[j]][i]
            print line.replace('*', capInput[j]),
            if j == len(capInput)-1: print
    print '\n'

msg = raw_input("Make bigger: ")
makeBigLetters(msg)
