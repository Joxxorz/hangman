import words
from random import randint

compKnows = []
blank = "-"

def getWord():
    noWords = len(words.words) - 1
    word = words.words[randint(0,noWords)]
    letters = word.split()
    for letters in word:
        compKnows.append(blank)
    return word
def checkChar(userGuess, theAnswer, lives):
    if userGuess in theAnswer:
        finalAnswer = displayAnswers(userGuess, theAnswer)
        return finalAnswer
    else:
        print('Sorry that character wasn\'t in my word!')
        lives = lives - 1
        print('You have '+ str(lives) +' lives remaining.')
        return lives
def displayAnswers(userGuess, theAnswer):
    letters = theAnswer.split()
    for letters in theAnswer:
        loc = theAnswer.index(letters)
        if userGuess == letters:
            compKnows[loc] = userGuess
    print compKnows
    compKnowsFinal = "".join(compKnows)
    return compKnowsFinal
def replayGame():
    print('Would you like to play again?')
    userReplay = raw_input('Enter Y for yes, N for no:')
    if userReplay == "Y":
        compKnows = None;
        playGame()
    else:
        return
def playGame():
    lives = 5
    userAnswer = None
    userAnswer = []
    finalAnswer = None
    finalAnswer = ""
    compKnowsFinal = None
    compKnowsFinal = ""
    del lst[:]
    compKnows = []

    print('Hi! Lets play hangman!')
    theAnswer = getWord()

    print('The word to guess has ' + str(len(theAnswer)) + ' characters.')
    print('Guess a character to get started!')

    while True:
        userGuess = str(raw_input('Your guess: '))
        userGuess = userGuess.upper()
        if finalAnswer != theAnswer:
            if lives == 0:
                print('I\'m sorry, you have lost.')
                break
            else:
                resultish = checkChar(userGuess, theAnswer, lives)
                if isinstance( resultish, int ):
                    lives = resultish
                else:
                    finalAnswer = resultish

                if finalAnswer == theAnswer:
                    print('You\'ve won!')
                    break
        else:
            print('You\'ve won!')
            break

    replayGame()

playGame()
