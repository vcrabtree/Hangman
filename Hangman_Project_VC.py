# Vera Crabtree 11/5/18 To implement a game of hangman

from random import *

def chooseRandomWord(wordList):
    '''
    Select a string from a list of strings
    Args: wordList
    Return: wordlist[randWord]
    '''
    randWord = randint(0,len(wordList)-1)
    return wordList[randWord]

def getBlankList(correctWord):
    '''
    Creates blank word display
    Args: correctWord
    Returns: wordDisplay 
    '''
    wordDisplay = '_' * len(correctWord)
    wordDisplay = list(wordDisplay)
    return wordDisplay

def getLetterFromUser():
    '''
    Get single lowercase letter between a to z
    Args: none
    Return: single letter 
    '''
    letter = input("Please enter a single letter between a and z:")
    while (len(letter) != 1) or (letter not in 'abcdefghijklmnopqrstuvwxyz'):
        letter = input("Please enter a single letter between a and z:")
    return letter

def userGuess(correctWord, letterGuess): 
    '''
    Will determine if guess is True or False
    Args: guess
    Return: Boolean
    '''
    correctWord = list(correctWord)
    if letterGuess in correctWord:
        return True
    else:
        return False

def isWin(wordDisplay): 
    '''
    Determine if player won
    Args: wordDisplay
    Return: Boolean
    '''
    if '_' in wordDisplay:
        return False
    return True

def drawBody(badGuess):
    '''
    Draws body part for wrong guess
    Args: bad guess
    Returns: bad guess
    '''
    if badGuess == 1:
        print("Draw body part: head")
    elif badGuess == 2:
        print("Draw body part: body")
    elif badGuess == 3:
        print("Draw body part: left arm")
    elif badGuess == 4:
        print("Draw body part: right arm")
    elif badGuess == 5:
        print("Draw body part: left leg")
    elif badGuess == 6:
        print("Draw body part: right leg")
    return badGuess

def displayBody():
    '''
    Display the body.
    Args: None
    Returns: None
    '''
 
    print("""
     ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           

    """)


def main():
    '''
    Implementation of hangman game
    Args: none
    Return: none
    '''
    wordList = ['dog', 'cowboy', 'computer', 'water', 'penguin', 'pineapple', 'nature']
    badGuess = 0
    word = chooseRandomWord(wordList)
    blankWord = getBlankList(word)
    print("Welcome to the game of hangman. Here is your word:")
    print(' '.join(blankWord))
    win = False
    while win != True:
        guess = getLetterFromUser()
        testGuess = userGuess(word, guess)
        if testGuess == True:
            for i in range(len(word)):
                if guess == word[i]:
                    blankWord[i] = guess
        print(' '.join(blankWord))
        win = isWin(blankWord)
        if win == True:
            print("You win!")
        else:
            if testGuess == False:
                badGuess = badGuess + 1 
                badGuess = drawBody(badGuess)
                if badGuess == 7:
                    print("You lose. The word was:", word)
                    displayBody()
                    break
    
def testFunctions():
    '''
    Tests each of the functions
    Args: none
    Returns: none
    '''
    
    # Choose Random Word from List
    list1 = ['dog', 'cat', 'rat']
    test1 = chooseRandomWord(list1)
    if test1 == 'dog' or test1 == 'cat' or test1 == 'rat':
        print("Passed chooseRandomWord test")
    else:
        print("Failed chooseRandomWord test")

    # Print blank list for word
    word = 'dog'
    test2 = getBlankList(word)
    if test2 == ['_', '_', '_']:
        print("Passed getBlankList test")
    else:
        print("Failed getBlankList test")

    # Gets a single lowercase letter from user
    print("Type 'Am' then 'd'")
    test3 = getLetterFromUser()
    if test3 == 'd':
        print("Passed getLetterFromUser test")
    else:
        print("Failed getLetterFromUser test")

    # Determine if user letter guess is in word
    word = 'dog'
    name = 'o'
    test4 = userGuess(word, name)
    if test4 == True:
        print("Passed userGuess test")
    else:
        print("Failed userGuess test")

    # Determine if user won
    wordDisplay = ['_', 'o', '_']
    test5 = isWin(wordDisplay)
    if test5 == False:
        print("Passed isWin test")
    else:
        print("Failed isWin test")
    wordDisplay2 = ['d', 'o', 'g']
    test6 = isWin(wordDisplay2)
    if test6 == True:
        print("Passed isWin test")
    else:
        print("Failed isWin test")

    # Draw body part if guess is False
    badGuess = 4
    test7 = drawBody(badGuess)
    if test7 == 4:
        print("Passed drawBody test")
    else:
        print("Failed drawBody test")

main()







