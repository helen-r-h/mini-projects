import random 

# generate a random number 
def roll(): # reusable block of code
    min_ =  1
    max_ = 6
    roll = random.randint(min_, max_)

    return roll

# set up the game - checking players, max score, player scores

while True: 
    players = input("Enter the num of players(2-4): ")
    if players.isdigit(): # checks if players is a digit
        players = int(players)
        if 2 <=players <= 4:
            break 
        else:
            print("Must be something that is in the range of 2 to 4, try again.")
            continue
    else:
        print("This is not the correct input, try again.")
        continue

max_score = 50
player_scores = [0 for _ in range(players)] # this is list comprehension
# [13, 40, 32]

# playing the game

while max(player_scores) < max_score:
    
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!\n")
        print("Your total socre is:", player_scores[player_index], "\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break   
            value = roll()
            if value == 1: 
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is", current_score)

        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])

max_score = max(player_scores)
winning = player_scores.index(max_score)
print("Player", winning + 1, "is the winner with the score of: ", max_score)
