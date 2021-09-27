#Hangman

from random import choice
from display import hangedman

playerScore = 0
computerScore = 0

def start(playerScore, computerScore):
    print("LET THE GAME BEGIN")
    game(playerScore, computerScore)

#Fucntion that handles the main loop of the game.
def game(playerScore, computerScore):
    userWord = input("Enter your word: ")
    wordLength = len(userWord)
    clue = wordLength * "_"
    tries = 6
    lettersTried = ""
    wrongLetters = 0

    while (wrongLetters != tries) and (clue != userWord):
        letter = guessLetter()
        #If the guess is 1 character long and is a letter:
        if len(letter) == 1 and letter.isalpha():
            #If the letter isn't found, then find() returns -1. This means -1 + 1 = 0 which is equivalent to False.
            if lettersTried.find(letter) + 1:
                print("This letter has already been chosen...")
            else:
                lettersTried += letter
                firstIndex = userWord.find(letter)
                #If the guess isn't in the user's word it adds to the wrongLetters counter.
                if firstIndex == -1:
                    wrongLetters += 1
                    print("NOPE...HA!")
                else:
                    print(f"Congratulations, {letter} is correct!")
                    #Replaces _ with the letter if it is in the word.
                    for i in range(wordLength):
                        if letter == userWord[i]:
                            clue = clue[:i] + letter + clue[i+1:]
        else:
            print("Choose something else please: ")
        #Outputs the display from hangedman() by entering the parameter wrongLetters - 1 as an index.
        if(wrongLetters) > 0:
            hangedman(wrongLetters - 1)

        print(clue)
        print(f"Guesses: {lettersTried}")

        if wrongLetters == tries:
            print("GAME OVER!")
            print(f"The word was: {userWord}")
            computerScore += 1
            break
        if clue == userWord:
            print("YOU WIN!")
            print(f"{userWord} was the word! Well done")
            playerScore += 1
            break
    playAgain(playerScore, computerScore)

#Function that asks the user for their guess.
def guessLetter():
    print("")
    letter = input("Take a guess, insert a letter: ").strip().lower()
    print("")
    return letter

#Function that asks the player if they want to start again or not and carries out the appropriate response.
def playAgain(playerScore, computerScore):
    scores(playerScore, computerScore)
    print("")
    retryAnswer = input("Play again? Y/N: ")
    if retryAnswer in("y", "Y", "Yes", "yes", "Of Course!"):
        start(playerScore, computerScore)
    else:
        print("Thanks for playing - Until next time....")
        return False

#Function that states the scores of every game.
def scores(playerScore, computerScore):
    print("SCORES")
    print(f"Player: {playerScore}")
    print(f"Computer: {computerScore}")

start(playerScore, computerScore)
