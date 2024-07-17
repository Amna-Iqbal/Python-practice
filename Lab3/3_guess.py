import random
our_number = random.randint(1, 9)

while True:
    users_guess = int(input("Guess a number between 1 to 9: "))
    if users_guess==our_number:
        print("Well guessed ! ")
        break
    else:
        print("Wrong Guess! Try Again")
    
