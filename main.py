import random

print('hi, ready to play?')

guessesTaken = 0

print("what's your name player?")

myName = input()

randomNumber = random.randint(1,20)

print("Well "+myName+ "i am of a number between 1 and 20 take a guess!!")

while guessesTaken < 6:
    print("take a guess")

    guess = input()

    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if  guess < randomNumber:
        print('Your guess is too low.')

    if guess > randomNumber:
        print('Your guess is too high.')

    if guess == randomNumber:
        break

if guess ==randomNumber:

    guessesTaken = str(guessesTaken)

    print("Good job "+myName +" you guessed my number in "+guessesTaken+ " guesses")

if guess != randomNumber:

    randomNumber = str(randomNumber)
    print("Nope. the number i was thinking of is "+ randomNumber)