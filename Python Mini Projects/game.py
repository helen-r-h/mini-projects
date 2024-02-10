# generate a 4 color random code using module random

import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code(): # this generates a 4 digit color code using a for loop that iterates 4 times from CODE_LENGTH
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS) # randomly select from colors list
        code.append(color)

    return code


# make the user guess the code - give feedback (invalid)

def guess_code(): 
    while True:
        guess = input("Guess: ").upper().split(" ") # makes user input upper case and makes list 

        if len(guess) != CODE_LENGTH:
            print("You must guess", CODE_LENGTH, "colors.")
            continue

        for user_color in guess:
            if user_color not in COLORS:
                print("Invalid color, try again.")
                break  # break out of for loop if the color is not valid

        else: 
            break # gets out of the while loop if the user input is 

    return guess

# compare guess using incorrect and correct position

def check_code(guess, real_code):
    #check the correct position
    color_counts = {}
    correct_position = 0
    inccorect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        


    #check the incorrect position

# tie the game together using loops, determine if user lost game, 10 tries