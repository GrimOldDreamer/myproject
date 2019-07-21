#Modules
import random #for random dice rolling and coin flips#

#Define Functions

def main_menu():

    print("Hello! Here is main menu!\n")
    print("1. Dice Roller\n"
          "2. Testing tool\n"
          "3. Close program\n")

    choice = input('Choose what you need\n')

    if choice == "1":
        dice_roller()
        main_menu()
    elif choice == "2":
        testing_tool()

def dice_roller():
    #variables
    qt = int(input("How many Dices do you rolling\n"))
    d = int(input("Enter your Dice type\n"))
    i = 0
    summ: int = 0
    answer: str = 'y'
    while answer == 'y':
        while qt != i:
            roll = random.randrange(1,d)
            print("You rolling : ", roll)
            i+=1
            summ += roll
        print("Summary is : ",summ)
        answer: str = input("\nDo you wanna make a roll?  (y/n)\n")
        if answer == ('y'.lower()):
            i = 0
            qt = int(input("How many Dices do you rolling\n"))
            d = int(input("Enter your Dice type\n"))
    input("Press any key to come back in main menu")

def testing_tool():
    print("""Welcome to the testing tool
You can easy testing your combat mechanics here and stats also!""")

main_menu()