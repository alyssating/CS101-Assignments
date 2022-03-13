"""
Created on 9/10/2021

@author: alyssa
"""
import random

def part_curly_hair():
    '''
    Returns a string that is curly hair.
    '''
    hCurly = r" GGGGGGGGGGGGGGGG "
    return hCurly

def part_straight_hair():
    '''
    Returns a string that is straight hair.
    '''
    hStraight = r" ---------------- "
    return hStraight

def part_crazy_hair():
    '''
    Returns a string that is crazy hair.
    '''
    hCrazy = r" /\/Y\/Y\/Y\/Y\/\ "
    return hCrazy

def part_short_nose():
    '''
    Returns a string that is a short nose.
    '''
    nShort = r" |              | " + "\n"
    nShort += r" |      /\      | " + "\n"
    nShort += r" |     /nn\     | "
    return nShort

def part_long_nose():
    '''
    Returns a string that is a long nose.
    '''
    nLong = r" |              | " + "\n"
    nLong += r" |      /\      | " + "\n"
    nLong += r" |     |  |     | " + "\n"
    nLong += r" |     |  |     | " + "\n"
    nLong += r" |     |nn|     | "
    return nLong

def part_wavy_nose():
    '''
    Returns a string that is a wavy nose.
    '''
    nWavy = r" |              | " + "\n"
    nWavy += r" |      /\      | " + "\n"
    nWavy += r" |     (  )     | " +"\n"
    nWavy += r" |     (nn)     | "
    return nWavy

def part_smile_mouth():
    '''
    Returns a string that is a smiley mouth.
    '''
    mSmile = r" |              | " + "\n"
    mSmile += r" |     \__/     | "
    return mSmile

def part_frown_mouth():
    '''
    Returns a string that is a frowny mouth.
    '''
    mFrown = r" |              | " + "\n"
    mFrown += r" |     /--\     | "
    return mFrown

def part_straight_mouth():
    '''
    Returns a string that is a straight mouth.
    '''
    mStraight = r" |              | " + "\n"
    mStraight += r" |    (----)    | "
    return mStraight

def part_shut_eyes():
    '''
    Returns a string that is shut eyes.
    '''
    eShut = r" |   --    --   | "
    return eShut

def part_triangle_eyes():
    '''
    Returns a string that is triangle eyes.
    '''
    eTriangle = r" |    ^    ^    | "
    return eTriangle

def part_round_eyes():
    '''
    Returns a string that is round eyes.
    '''
    eRound = r" |   ()    ()   | "
    return eRound

def happy_head():
    '''
    Print a head that looks like it's happy,
    With happy eyes and a smile.
    '''

    print (part_curly_hair())
    print (part_triangle_eyes())
    print (part_short_nose())
    print (part_smile_mouth())

    return ""

def sad_head():
    '''
    Print a head that looks like it's happy,
    With sad eyes and a frown.
    '''

    print (part_straight_hair())
    print (part_shut_eyes())
    print (part_long_nose())
    print (part_frown_mouth())

    return ""

def surprised_head():
    '''
    Print a head that looks like it's surprised,
    With wide eyes and an open mouth.
    '''

    print (part_crazy_hair())
    print (part_round_eyes())
    print (part_wavy_nose())
    print (part_straight_mouth())

    return ""

def bored_head():
    '''
    Print a head that looks like it's bored,
    With shut eyes and a neutral mouth.
    '''

    print (part_straight_hair())
    print (part_shut_eyes())
    print (part_short_nose())
    print (part_straight_mouth())

    return ""

def mixed_head():
    '''
    Print a head that looks happy on the top half and upset on the bottom,
    With happy eyes and a frowny mouth.
    '''

    print (part_crazy_hair())
    print (part_triangle_eyes())
    print (part_wavy_nose())
    print (part_frown_mouth())

    return ""

def totem_fixed():
    '''
    Print the same totem pole with three of the same head,
    the happy head.
    '''

    happy_head()
    mixed_head()
    sad_head()

def head_with_mouth(mouthfunc):
    '''
    Print a head with curly hair, triangle eyes, and a short nose,
    but with a mouth specified by mouthfunc.
    '''

    print (part_curly_hair())
    print (part_triangle_eyes())
    print (part_short_nose())
    print (mouthfunc())

    return ""

def head_with_hair(hairfunc):
    '''
    Print a head with shut eyes, a wavy nose, and a smiley mouth,
    but with hair specified by hairfunc.
    '''

    print (hairfunc())
    print (part_shut_eyes())
    print (part_wavy_nose())
    print (part_smile_mouth())

    return ""

def head_with_eyes(eyefunc):
    '''
    Print a head with straight hair, a long nose, and a frowny mouth,
    but with eyes specified by eyefunc.
    '''

    print (part_straight_hair())
    print (eyefunc())
    print (part_long_nose())
    print (part_frown_mouth())

def selfie_band():
    '''
    Returns with a string that is a selfie band with my NetID in it.
    '''

    sBand = r" +--------------+ " + "\n"
    sBand += r" |at341    at341| " + "\n"
    sBand += r" +--------------+ "
    return sBand

def selfie(hairfunc,eyefunc):
    '''
    Helper function that prints a head with my selfie band in it,
    with a short nose and smile mouth but eyes specified by eyefunc
    and hair specified by hairfunc.
    '''

    print (hairfunc())
    print (selfie_band())
    print (eyefunc())
    print (part_short_nose())
    print (part_smile_mouth())

    return ""

def totem_selfie():
    '''
    Print a totem pole with a selfie band
    by calling the selfie() helper function
    '''

    selfie(part_straight_hair,part_triangle_eyes)
    selfie(part_curly_hair, part_shut_eyes)
    selfie(part_crazy_hair, part_round_eyes)

    return ""

def head_random():
    '''
    Print a head with randomly chosen
    hair.
    '''

    x = random.randint(1,3)
    if x == 1:
        hairfunc = part_crazy_hair
    elif x == 2:
        hairfunc = part_curly_hair
    else:
        hairfunc = part_straight_hair

    head_with_hair(hairfunc)

    return ""

def totem_random():
    '''
    Print three random heads using head_random()
    '''

    head_random()
    head_random()
    head_random()

if __name__ == '__main__':
    print("\nfixed totem\n")

    totem_fixed()

    print("\nself totem\n")

    totem_selfie()

    print("\nrandom totem\n")

    totem_random()
