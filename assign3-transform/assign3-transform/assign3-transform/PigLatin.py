"""
Created on 10/13/2021

@author: alyssa ting
"""

def startsWithVowel(word):
    """
    Checks to see if the word starts with a vowel.
    """
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return True
    else:
        return False


def firstVowelIndexQu(word):
    """
    Returns the index of the first vowel of a word
    if the word starts with "qu."
    """
    vowels = "aeiouAEIOU"
    dex = 2
    for char in word[2:]:
        dex += 1
        if char in vowels:
            dex = dex - 1
            return dex

def firstVowelIndex(word):
    """
    Returns the index of the first vowel of a word
    if the word starts with a consonant.
    """
    vowels = "aeiouAEIOU"
    dex = 0
    for char in word:
        dex += 1
        if char in vowels:
            dex = dex - 1
            return dex
    if len(word) == dex:
        dex = -1
        return dex # returns -1 if the whole word is consonants

def startsWithQu(word):
    """
    Checks to see if a word starts with "qu."
    """
    if word[0] == "q" and word[1] == "u":
        return True
    else:
        return False

def encrypt(phrase):
    """
    Given a string as the parameter phrase,
    returns a string of phrase translated
    into pig latin given the rules described
    in the assignment.
    """
    ret = []
    vowels = "aeiouAEIOU"
    for word in phrase.split():
        if startsWithVowel(word):
            word = word + "-way"
            ret.append(word)
        elif startsWithVowel(word) == False:
            if firstVowelIndex(word) == -1:
                dex = word.find("y")
                if dex == -1 or dex == 0:
                    word = word + "-way"
                    ret.append(word)
                else:
                    word = word[dex:] + "-" + word[:dex] + "ay"
                    ret.append(word)
            elif startsWithQu(word):
                if word[2] not in vowels:
                    dex = firstVowelIndexQu(word)
                    word = word[dex:] + "-" + "qu" + word[dex-1] + "ay"
                    ret.append(word)
                else:
                    dex = firstVowelIndexQu(word)
                    word = word[dex:] + "-" + "quay"
                    ret.append(word)
            else:
                dex = firstVowelIndex(word)
                word = word[dex:] + "-" + word[:dex] + "ay"
                ret.append(word)
    return " ".join(ret)

def decrypt(phrase):
    """
    Given a string as the parameter phrase,
    returns a string of phrase translated
    from pig latin to normal English given
    the rules described in the assignment.
    """
    ret = []
    for word in phrase.split():
        if word[-3:] == "way":
            if len(word.split("-")) > 2:
                word = word.split("-")[0] + "-" + word.split("-")[1]
                ret.append(word)
            else:
                word = word.split("-")[0]
                ret.append(word)
        else:
            if len(word.split("-")) > 2:
                firstWord = word.split("-")[-1][:-2] + word.split("-")[0]
                word = firstWord + "-" + word.split("-")[1]
                ret.append(word)
            else:
                word = word.split("-")[-1][:-2] + word.split("-")[0]
                ret.append(word)

    return " ".join(ret)


if __name__ == '__main__':
    print(decrypt(encrypt("anchor oasis umbrella AWOL computer yesterday STRENGTH my rhythm 'always!' quiz queue quay quran")))
    print(decrypt(encrypt("The Bears lost to the Packers today in on Football Sunday.")))
    print(decrypt(encrypt("You must create a module named PigLatin.py. Make sure you create it with a main program block.")))
    print(decrypt(encrypt("I made one-thousand paper cranes today.")))