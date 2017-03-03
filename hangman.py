"""
Save their chosen character to a string
Check if character is in the word
    if it is, say it is then demo like i.e. _ _ a _ _

On user win, congratulate user
Ask user if they want to play again
"""

lives = 5

def getWord():
    word = 'TEST'
    return word

def checkChar(userGuess, theAnswer, lives):
    if userGuess in theAnswer:
        displayAnswers(userGuess, theAnswer)
        return lives
    else:
        print('Sorry that character wasn\'t in my word!')
        lives = lives - 1
        print('You have '+ str(lives) +' lives remaining.')
        return lives

def displayAnswers(userGuess, theAnswer):
    letters = theAnswer.split()
    for letters in theAnswer:
        if userGuess == letters:
            userAnswer.insert(letters.index(userGuess), letters)
            print(userAnswer)
        else:
            print "-"

print('Hi! Lets play hangman!')
theAnswer = getWord()
userAnswer = []

print('The word to guess has ' + str(len(theAnswer)) + ' characters.')
print('Guess a character to get started!')

while True:
    userGuess = str(raw_input('Your guess: '))
    userGuess = userGuess.upper()
    if userAnswer != theAnswer:
        if lives == 0:
            print('I\'m sorry, you have lost.')
            break
        else:
            lives = checkChar(userGuess, theAnswer, lives)
    else:
        break
