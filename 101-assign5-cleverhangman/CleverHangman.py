'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: AlyssaTing    at341
'''

import random, os, sys

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    
    print ("How many misses do you want? Hard has 8 and Easy has 12.")
    x = input ("(h)ard or (e)asy> ") #don't worry about user putting in anything other than 'h' or 'e'
    if x == "h":
        return 8
    return 12

def handleUserInputDebugMode():
    '''
    This function asks the user if they would like to play the game in debug mode.
    '''
    x = input ("Which mode do you want: (d)ebug or (p)lay: ")
    if x == "d":
        return True
    return False

def handleUserInputWordLength():
    '''
    This function asks the user how long the secretWord should be.
    '''

    x = input ("How many letters in the word you'll guess: ")
    return int(x)

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''

    x = input("letter> ")
    while x in lettersGuessed:
        print("you already guessed that")
        x = input("letter> ")
    return x

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    displayString = "letters not yet guessed: "
    for ch in alphabet:
        if ch in lettersGuessed:
            displayString += " "
        else:
            displayString += ch
    displayString += "\n"
    displayString += "misses remaining = " + str(missesLeft) + "\n"
    displayString += " ".join(hangmanWord)
    return displayString

def createTemplate(currTemplate, letterGuess, word):
    '''
    This function creates a new template for the secret word that the user will see.
    '''
    newTemplate = []
    for dex in range(len(word)):
        if word[dex] == letterGuess:
            newTemplate.append(word[dex])
        elif currTemplate[dex] != "_":
            newTemplate.append(currTemplate[dex])
        else:
            newTemplate.append("_")
    return "".join(newTemplate)

def getNewWordList (currTemplate, letterGuess, wordList, debug):
    '''
    This function constructs a dictionary of strings as the key to lists as the value.
    It returns a 2-tuple, where the first element is the template corresponding to the
    largest group of words, and the second element is the list of words that
    match this template.
    '''
    dict = {}
    for word in wordList:
        k = createTemplate(currTemplate,letterGuess,word)
        if k not in dict:
            dict[k] = []
        dict[k].append(word)
    ret = sorted(sorted (dict.keys(), key = lambda x: x.count("_"), reverse = True), key = lambda y: len(dict[y]), reverse = True)
    if debug:
        for temp in sorted(dict.keys()):
            print (temp + " : " + str(len(dict[temp])))
        print ("# keys = " + str(len(dict.keys()))) # it's doing this twice each time
        print ("# possible words: "+ str(len(dict[ret[0]])))
    return (ret[0],dict[ret[0]])

def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    '''
    This function takes the information from the parameters and  indicates
    whether the user missed. Returns a list with the following at each index:
    Index 0: updated value for missesLeft
    Index 1: indication whether the user made a correct guess
    '''

    if guessedLetter in hangmanWord:
        missesLeft = missesLeft
        bool = True
    else:
        missesLeft -= 1
        bool = False
    return [missesLeft,bool]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    # importing words from the file and putting them into a list
    f = open(filename)
    wordsList = [w.strip() for w in f.read().split()]

    # seeing if the user wants to play in debug mode
    debug  = handleUserInputDebugMode()

    # finding the first secret word:
    length = handleUserInputWordLength()
    eligibleWords = [w for w in wordsList if len(w) == length]

    # determining the amount of misses
    missesTotal = handleUserInputDifficulty()
    missesLeft = missesTotal

    # determining the first secret word
    secretWord = random.choice(eligibleWords)

    # creating the first hangmanWord
    hangmanWord = []
    for x in range(length):
        hangmanWord.append("_")
    lettersGuessed = []

    # while loop for the game after the initial conditions are set up
    while missesLeft > 0 and "_" in hangmanWord:

        dString = createDisplayString(lettersGuessed,missesLeft,hangmanWord)
        print (dString)
        if debug:
            print ("(word is " + secretWord + ")")
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,dString)
        lettersGuessed.append(guessedLetter)
        callingGNWL = getNewWordList(hangmanWord, guessedLetter, eligibleWords, debug)
        eligibleWords = callingGNWL[1]
        hangmanWord = callingGNWL[0]

        # choosing a new secretWord from the new list of eligible words
        secretWord = random.choice(eligibleWords)
        missesLeft = processUserGuessClever(guessedLetter, hangmanWord,missesLeft)[0]
        if processUserGuessClever(guessedLetter, hangmanWord,missesLeft)[1] == False:
            print ("you missed: " + guessedLetter + " is not in word")

    guessesMade = len(lettersGuessed)
    missesMade = missesTotal - missesLeft

    if "_" not in hangmanWord:
        won = True
        print ("you guessed the word: " + secretWord)
        print ("you made " + str(guessesMade) + " guesses with " + str(missesMade) + " misses")

    else:
        won = False
        print ("you're hung!!" + "\n" + "word is " + secretWord)
        print ("you made " + str(guessesMade) + " guesses with " + str(missesMade) + " misses")

    return won

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    gamesToPlay = 1
    gamesWon = 0
    gamesLost = 0

    while gamesToPlay == 1:
        game = runGame('lowerwords.txt')
        if game:
            gamesWon += 1
        else:
            gamesLost += 1
        y = input("Do you want to play again? y or n> ")
        while y != "y" and y != "n":
            print ("please type in either a y or an n.")
            y = input("Do you want to play again? y or n> ")
        if y == "y":
            gamesToPlay = 1
        elif y == "n":
            gamesToPlay = 0

    print ("You won " + str(gamesWon) + " game(s) and lost " + str(gamesLost))