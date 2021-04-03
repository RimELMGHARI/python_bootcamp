
import random

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

x= random.randint(1, 99)
print(x)
y= int(input("What's your guess between 1 and 99?\n ->"))
s=1

while y!=x:
    if y<x:
        print("Too low!")
        s+=1
    
    if y>x:
        print("Too high!")
        s+=1
    
    y= int(input("What's your guess between 1 and 99?\n->"))
    

if y==x and s!=1:
    print("Congratulations, you've got it! \nYou won in", s ,"attempts!")

if y==x and s==1:
    print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
