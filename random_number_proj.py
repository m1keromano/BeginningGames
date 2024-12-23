import random
number = random.randrange(1, 10)
playing = True 

while playing == True:
    guess = int(input("Guess a number: "))
    if guess > number: 
        print("Your guess is too high")

    if guess < number: 
        print("Your guess is too low")

    if guess == number: 
        playing = False
        print("You guessed correctly!")