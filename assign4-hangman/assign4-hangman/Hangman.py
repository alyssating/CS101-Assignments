'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: AlyssaTing    at341
'''

import random

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

def getWord(words, length):
    '''
    Selects the secret word that the user must guess.
    This is done by randomly selecting a word from words that is of length length.
    '''

    eligibleWords = [w for w in words if len(w) == length]
    randomInt = random.randint(0,len(eligibleWords)-1)
    secretWord = eligibleWords[randomInt]
    return secretWord

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    lettersGuessed.sort()
    displayString = "letters you've guessed: "+ " ".join(lettersGuessed) + "\n"
    displayString += "misses remaining = " + str(missesLeft) + "\n"
    displayString += " ".join(hangmanWord)
    return displayString


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    print (displayString)
    x = input("letter> ")
    while x in lettersGuessed:
        print ("you already guessed that")
        x = input("letter> ")
    return x

def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    if guessedLetter in secretWord:
        guessedLetterIndexes = []
        listSecretWord = list(secretWord)
        for x in range(len(listSecretWord)):
            if listSecretWord[x] == guessedLetter:
                guessedLetterIndexes.append(x)
        for dex in guessedLetterIndexes:
            hangmanWord[dex] = guessedLetter
        return hangmanWord
    else:
        return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''

    newHangmanWord = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    if guessedLetter not in secretWord:
        updatedMissesLeft = missesLeft - 1
        indexTwoBool = False
    else:
        updatedMissesLeft = missesLeft
        indexTwoBool = True

    list = [newHangmanWord,updatedMissesLeft,indexTwoBool]
    return list

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    f = open(filename)
    wordsList = [w.strip() for w in f.read().split()]

    missesTotal = handleUserInputDifficulty()
    print("you have " + str(missesTotal) + " misses to guess word.")
    missesLeft = missesTotal

    length = random.randint(5,10)
    secretWord = getWord(wordsList,length)

    hangmanWord = []
    for x in range(length):
        hangmanWord.append("_")
    lettersGuessed = []

    while missesLeft > 0 and "_" in hangmanWord:

        displayString = createDisplayString(lettersGuessed,missesLeft,hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,displayString)
        lettersGuessed.append(guessedLetter)
        hangmanWord = processUserGuess(guessedLetter, secretWord, hangmanWord,missesLeft)[0]
        missesLeft = processUserGuess(guessedLetter, secretWord, hangmanWord,missesLeft)[1]
        if processUserGuess(guessedLetter, secretWord, hangmanWord,missesLeft)[-1] == False:
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