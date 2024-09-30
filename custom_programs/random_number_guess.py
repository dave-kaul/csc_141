# A Random number chooser
# Dave Kaul

import random
magicNumber = int(random.random() * 100)
num_tries = 0
 # We need to see if your number is the same as the magic number, too high, or too low
while True:

    your_answer = input("Please guess a number from 1-100: ")
    your_answer = int(your_answer)
    # Increase the counter of number of tries
    num_tries = num_tries + 1
    if your_answer == magicNumber:
        print ("You have won")
        print (f"You took {num_tries} tries to win the game.")
        break
    elif magicNumber < your_answer:
        print ("Too high")
    else:
        print ("Too Low")
