import random
print("Welcome to rock, paper scissors")
while True:
    cc=random.choice(['r', 'p', 's'])
    uc=(input("Enter your choice r, p, s")).lower()
    if cc==uc:
        print("Its a tie!")
    elif cc=='r' and uc=='s':
        print("you lose...")
    elif cc=='s' and uc=='p':
        print("you lose...")
    elif cc=='p' and uc=='r':
        print("you lose...")
    elif cc=='s' and uc=='r':
        print("you win !")
    elif cc=='p' and uc=='s':
        print("you win !")
    elif cc=='r' and uc=='p':
        print("you win !")
    else:
        print("Invalid input... retry")
    re=input("do you want to play again (y/n)").lower()
    if re=='n':
        print("byeeeeeeeee")
        break

        
