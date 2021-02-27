# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter 
        else:
            guessed += '_'
        guessed += ' '
    return guessed

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabetics = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        alphabetics = alphabetics.replace(letter, '')
    return alphabetics

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {0} letters long.'.format(len(secretWord)))
    
    tries = 8
    lettersGuessed = []
    wordGuessed = ''
    
    while(True):
        print('-------------')
        
        if(isWordGuessed(secretWord, lettersGuessed)):
            print('Congratulations, you won!')
            break
        elif tries == 0:
            print('Sorry, you ran out of guesses. The word was '+ secretWord + '.')
            break
        
        print('You have {0} guesses left.'.format(tries))
        print('Available letters: '+ getAvailableLetters(lettersGuessed))
        newletter = input('Please guess a letter:  ')
        
        if newletter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: '+ wordGuessed)
        else:
            lettersGuessed.append(newletter)
            wordGuessed = getGuessedWord(secretWord, lettersGuessed)
            if newletter in secretWord:
                print('Good guess: '+ wordGuessed)
            else:
                print('Oops! That letter is not in my word: '+ wordGuessed)
                tries -= 1
        
        
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
