import random

def guesser():
    num = random.randint(1, 100)
    i = 2
    while (i >= 0): 
        in_num = int(input("Guess a number between 1 to 100: "))
        if in_num > 100 or in_num < 1:
            print("Number exceeding the limit! Guess within 1 to 100.")
            continue
        elif in_num == num:
            print("You guessed the number!")
            break
        elif (i > 0):
            print(f"You guessed it wrong, You have {i} try(s) remaining.")
        else:
            print(f"You did not guess the number. The number was {num}.")
        i-=1

guesser()
