import random

inputValue=input("Enter a number")
if inputValue.isdigit():
    inputValue = int(inputValue)
    if inputValue<=0:
        print("Sorry, enter a positive number next time")
        quit()
else:
    print("Enter a number next time!")
    quit()
#random.randrange(1,100) #generate random number between 1 and 99
random_number=random.randint(0,inputValue) #generate random number between 0 and inputValue
guess=0
while True:
    guess+=1
    user_guess=input("Guess the number")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number next time")
        continue
    if user_guess==random_number:
        print("You guessed right!")
        continue
    else:
        print("You guessed wrong!")
    if user_guess>random_number:
        print("Sorry, you guessed higher!")
        continue
    elif user_guess<random_number:
        print("Sorry, you guessed lower!")
print("You got it in "+str(guess)+" guesses")