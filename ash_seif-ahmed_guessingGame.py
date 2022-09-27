
while(True):
    secretWord= input("Enter a Secret Word: ")
    guessLimit= int(input("Enter The Number of Available Guesses: "))
    guessCount=0
    outofGuesses= False
    guessedWord=""


    

    while guessedWord!=secretWord and not(outofGuesses):
        if guessCount<guessLimit:
            guessedWord= input("Enter The Guessed Word: ")
            guessCount+=1
            print(str(guessLimit-guessCount)+" Guesses left!")
        else:
            outofGuesses = True

    if outofGuesses:
        print("You Lost, Out of Guesses!")
    else:
        print("You Won!")

    key= input("Do You Want To Play Again? (Y/N): ")

    if not(key=="Y"):
        print("GoodBye!")
        break

    



