"""
Created on 11/14/2021

@author: alyss
"""
'''
This module is for you to use to test your implemention of the functions in Hangman.py

@author: rodger
'''

import CleverHangman

if __name__ == '__main__':

    print('Testing updateHangmanWord')
    guessedLetter = 'a'
    secretWord = 'cat'
    hangmanWord = ['c', '_', '_']
    expected = ['c', 'a', '_']
    print('Next line should be: ' + str(expected))
    print(Hangman.updateHangmanWord(guessedLetter, secretWord, hangmanWord))

