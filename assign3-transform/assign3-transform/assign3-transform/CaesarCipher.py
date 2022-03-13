"""
Created on 10/16/2021

@author: alyssa ting
"""
import os.path

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def encrypt(w):
    """
    Encrypts the string passed through the parameter w by the
    shift defined by setShift.
    """
    ret = ""
    for ch in w:
        if ch in lower_alph:
            dex = lower_alph.index(ch)
            ret += shifted_lower[dex]
        elif ch in upper_alph:
            dex = upper_alph.index(ch)
            ret += shifted_upper[dex]
        elif ch == " ":
            ret += " "
        else:
            ret += ch
    return ret

def setShift(int):
    """
    sets the values of the three global variables shift, shifted_lower, and
    shifted_upper depending on the int parameter to setShift.
    """

    global shift, shifted_lower, shifted_upper

    lower_alph = "abcdefghijklmnopqrstuvwxyz"
    upper_alph = lower_alph.upper()

    shift = int
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]

def findShift(st):
    """
    Takes a string of caeser cipher encrypted words as
    a parameter and returns the shift that was originally
    used to encrypt the words.
    """

    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]

    maxIntersection = 0
    maxShift = 0
    for i in range(26):
        setShift(i)
        ew = [encrypt(w) for w in st.split()]
        ewSet = set(ew)
        intersection = ewSet.intersection(set(wordsClean))
        overlap = len(intersection)
        if overlap > maxIntersection:
            maxIntersection = overlap
            maxShift = i

    return 26 - maxShift

if __name__ == '__main__':
    # test the encrypt function
    print(encrypt("Hello, my name is Alyssa Ting and I'm a 19-year-old student."))
    print(encrypt("It is so nice and sunny outside, it must be 20 degrees Celsius."))
    print(encrypt("I am very excited for the men's basketball season"))

    # testing the setShift and encrypt functions
    setShift(3)
    print(shift,encrypt("Hello, my name is Alyssa Ting and I'm a 19-year-old student."))
    setShift(10)
    print(shift,encrypt("Hello, my name is Alyssa Ting and I'm a 19-year-old student."))
    setShift(35)
    print(shift,encrypt("Hello, my name is Alyssa Ting and I'm a 19-year-old student."))

    # test the decrypt function
    setShift(7)
    print("shift of",shift, ":",encrypt("This weekend was Family Weekend at Duke"))
    print("shift found by function:", findShift("aopz dllrluk dhz Mhtpsf dllrluk ha Kbrl"))

    setShift(11)
    print("shift of",shift,":",encrypt("It's getting colder and colder these days."))
    print("shift found by function:", findShift("Te'd rpeetyr nzwopc lyo nzwopc espdp oljd."))

    setShift(23)
    print("shift of",shift,":",encrypt("I am going to study for midterms next week!"))
    print("shift found by function:", findShift("f xj dlfkd ql pqrav clo jfaqbojp kbuq tbbh!"))
