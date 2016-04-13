from nose.tools import *
from enigma import *

def test_encode_decode():
    """ tests that the program encodes and decodes to the same
            as the input """
    enig = Enigma(534, 10, 5, [3, 1, 3, 4, 1, 0, 2, 3, 4, 2])
    string = """A semi-enigma-machine-like cypher that uses 'rotors' to cypher
and decypher messages. It is more unlike the enigma machine than
it is alike, the wheelsspin one way to encode, the other to decode,
whereas the enigma machine always went forward, and paired keys.
This doesn't pair keys, nor does the cypher travel throught the rotors
and back after hitting a reflector. The wheel positions are setteable,
and as many wheels as you want can be added for extra 'cypherage'. This
also lacks the letter pairings, instead using a seed for random numbers
used to shift the charactersets passed through."""
    newstr = enig.encode(string)
    assert_equal(string, enig.decode(newstr))

def test_encode():
    """ tests that encoding works as expected (and is consistent with the
            same settings """
    enig = Enigma(534, 16, 8, [4, 6, 0, 7, 3, 0, 2, 3, 7, 0, 4, 2, 6, 1, 5, 5])
    string = """Hello, this is a test string. I will follow this with a return
bringing it onto a new line. I can do this forever, but I won't. Just
for a while."""
    encoded = """-)m>&)IKp[1`Sro$82[@_`TV&`f%}|<]a1R*\W4IEb6j@+':`R[.(1$vV4rTJ2
6V?5.;8q r%0p@+[Ir7-?rzIl;nV<4W7,PD[5-?;RE+~vR5-`i}>=z@S "eJ`8g:S:1ir
E0=<F0~/;6)."""

    assert_equal(encoded, enig.encode(string))

    endsettings = [5, 2, 2, 7, 3, 0, 2, 3, 7, 0, 4, 2, 6, 1, 5, 5]
    assert_equal(endsettings, enig.getrotsettings())
    

def test_decode():
    """ tests that the decoding works as expected (consistent) """
    enig = Enigma(534, 16, 8, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    string = """-)m>&)IKp[1`Sro$82[@_`TV&`f%}|<]a1R*\W4IEb6j@+':`R[.(1$vV4rTJ2
6V?5.;8q r%0p@+[Ir7-?rzIl;nV<4W7,PD[5-?;RE+~vR5-`i}>=z@S "eJ`8g:S:1ir
E0=<F0~/;6)."""
    decoded = """Hello, this is a test string. I will follow this with a return
bringing it onto a new line. I can do this forever, but I won't. Just
for a while."""

    enig.setrotsettings([5, 2, 2, 7, 3, 0, 2, 3, 7, 0, 4, 2, 6, 1, 5, 5])
    assert_equal(decoded, enig.decode(string))

    startsettings = [4, 6, 0, 7, 3, 0, 2, 3, 7, 0, 4, 2, 6, 1, 5, 5]
    assert_equal(startsettings, enig.getrotsettings())
    
def test_fail():
    """ tests that the messages will not match when decoded in 
            the wrong order """
    enig = Enigma()
    str1 = "Hellow"
    str2 = "Potato"
    en1 = enig.encode(str1)
    en2 = enig.encode(str2)
    de1 = enig.decode(en1)
    de2 = enig.decode(en2)

    assert_not_equal(str1, de1)
    assert_not_equal(str2, de2)

def test_flaw():
    """ tests that inputs will match outputs if 'rewound' using
            another input """
    # just thought of this flaw brought about by the rewinding of
    # the wheels, if words are the same length you can use them to 
    # skip over decoding another word, if it was to be used
    # in that way
    enig = Enigma()
    str1 = "Potato"
    str2 = "Tomato"
    en1 = enig.encode(str1)
    en2 = enig.encode(str2)
    de1 = enig.decode(en1)
    de2 = enig.decode(en1)

    assert_equal(de2, str1)
