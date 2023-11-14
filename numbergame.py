import random

#Generate a random number between 1 and 100
random_number = random.randint(1, 100)

#Initialise the number of guesses
num_guesses = 0

#Ask the user to guess until they guess correctly or run out of guesses
while num_guesses < 10:
    guess = int(input("guess a number from 1-100: "))
    num_guesses +=1

# Prints out if the user guesses correctly and breaks
    if guess == random_number:
        print("CONGRATULATIONS! You guessed the random number")
        break

#Prints out if the user's guess is lower than the answer
    elif guess < random_number:
        print("Your guess is too low")

#Prints out if the user's guess is higher than the answer
    else:
        print("Your guess is too high")

# Prints when the user runs out of guesses
    if num_guesses == 10:
        print("Sorry you ran out of guesses. The secret number was{}.".format(random_number))
 
        
