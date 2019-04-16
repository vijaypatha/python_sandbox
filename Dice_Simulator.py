''' 
Source: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
Rolling a Dice Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
'''

#psudocode
'''
roll once -> randomly choose between 1 and 6
print("random number")
should I roll again? Y/N? 
Y
roll -> randomly choose between 1 and 6
print("random number")

STEP 1: function to roll the dice -> produce a roll
STEP 2: function to ask and repeat Step 1
'''

import random

#STEP 1: Function to roll the dice and store the number rolled in a container.  
def roll():
    num_rolled = random.randint(1, 6)
    print("You rolled {} " .format(num_rolled))
roll()

# STEP 2:  
roll_again = input("Ready to roll the dice again")
if roll_again != 'q':
    num_rolled = random.randint(1, 6)
    print("You rolled {} " .format(num_rolled))
else:
    print("Stopped playing")


name = input("YOur name?")
print("your name is " + name)

# user inputs something and check 
clean_city = ["seattle", "saltlake"]
userInput = ""
while userInput != "q":
    userInput = input("Enter a city or Q to quite")
    if user_input != "q":
        for city in clean_city:
            if userInput == city:
                print("its on of the clean city")
                break

clean_city = ["seattle","salt lake"]
userInput = ""
while userInput != "q":
    userInput = input("Enter a city or q")
    if userInput != "q":
        for city in clean_city:
            print("your city is clear")
            break


list_of_names = ["Farina", "Madi", "Annie", "Max", "Vlad", "Punya", "Muhammad"]
second_list_of_names = []
counter = 0
while counter < len(list_of_names):
  second_list_of_names.append(list_of_names[counter])
  counter += 1
print (second_list_of_names)


list_of_names = ["Farina", "Madi", "Annie", "Max", "Vlad", "Punya", "Muhammad"]
print(len(list_of_names))
counter = 0
while counter < len(list_of_names):
    counter += 1
    print(counter)