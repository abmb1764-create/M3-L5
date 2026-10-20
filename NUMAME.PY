import random
print("Welcome to the random number game. I am thinking of a number between 1 and 9. It is up to you to guess it.")
num=(random.randint(0,9))
chance=3
while True:
    g=int(input("enter your guess"))
    if g==num:
        print("WOW! You got it!")
        break
    else:
        print("Try again")
        chance-=1
        if chance==0:
            print("You lose.. try again next time")
            break
