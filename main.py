import os
import random

# Data sources to pull from to create password

ABC_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC_UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SPECIAL_CHARS = ['!', '@', '#', '$', '%']

def pass_gen():

    num_chars = input("How many characters would you like the password to be?\n\n>>> ")
    
    if int(num_chars) < 0:
        print("Invalid selection. Please enter a positive number.")
        return
    
    new_pass = []

    for i in range(int(num_chars)):
        random_choice = random.randint(1, 4)

        if random_choice == 1:
            new_pass.append(random.choice(ABC_LOWER))
        elif random_choice == 2:
            new_pass.append(random.choice(ABC_UPPER))
        elif random_choice == 3:
            new_pass.append(random.choice(NUMBERS))
        else:
            new_pass.append(random.choice(SPECIAL_CHARS))

    print(new_pass)


pass_gen()