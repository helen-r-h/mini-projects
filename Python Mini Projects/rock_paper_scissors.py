import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ")
    if user_input.lower().strip() == "q":
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
        continue # reasks and starts the loop all over again

    random_num = random.randrange(0,3)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_num]
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1
       

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye.")
