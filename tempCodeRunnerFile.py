import random

#Function to roll the dice and store the number rolled in a container.  
def roll():
    num_rolled = random.randint(1, 6)
    print(num_rolled)
roll()