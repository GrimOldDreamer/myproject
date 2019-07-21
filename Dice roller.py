#Dice roller

#Modules
import random

#variables
qt = int(input("How many Dices do you rolling\n"))
d = int(input("Enter your Dice type\n"))
i = 0
roll = 0
summ = 0
answer = 'y'
while answer == 'y':
    while qt != i:
        roll = random.randint(1,6)
        print("You rolling : ",roll)
        i+=1
        summ +=roll
    print("Summary is : ", summ)
    answer = input("\nDo you wanna make a roll?  y/n\n")
    if answer == 'y':
        i = 0
        qt = int(input("How many Dices do you rolling\n"))
        d = int(input("Enter your Dice type\n"))

input("Press any key")
