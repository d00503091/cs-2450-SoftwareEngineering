import random

print("Hi! I am going to try to guess your age.")
name = input("Whats your name?")

guesses = []
guessed = False
guess_number = 0

while guessed == False:
    guess = random.randint(15,30)
    if guess in guesses:
        continue

    response = input( "are you " + str(guess)+ " years old?:")
    if response == 'y' or response == 'Y':
        print(f'haha!  {name} is {guess} years old!')
        guessed = True
    else:
        print("rats!")
        guess_number += 1
        guesses.append(guess)

    if guess_number > 10:
        break