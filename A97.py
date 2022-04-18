import random 

x = random.randint(1,9)
chance = 0
while chance < 5 :
    guess = int(input("Enter your guess-"))
    if guess == x:
        print("Congratulations.. YOU WIN !!")
        break
    else :
        print("Sorry.. TRY AGAIN !!",x)
    chance+=1

if not chance<5:
    print("YOU LOOOSE")