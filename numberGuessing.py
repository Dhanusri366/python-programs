import random

level = input("enter easy or hard:")
attempt =5
if(level == 'easy'):
    attempt = 10
ans = random.randint(1,100)
while(attempt>0):
    guess = int(input("enter a guess number: "))
    if(guess > ans):
        print("your guess is high")
    elif(guess<ans):
        print("your guess is low")
    else:
        print("you guessed the number!")
        break

