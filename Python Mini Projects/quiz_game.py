print("Welcome to my quiz game!")
playing = input("Would you like to play my game? ")

if playing.lower().strip() != "yes":
    print("Quit game. Thanks for playing.")
    quit()

print("Okay, let's play.")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :)))))")

answer = input("What is the highest mountain in the world? ")

if answer.lower().strip() == "everest":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :)))))")

answer = input("What does GPS stand for? ")

if answer.lower().strip() == "global positioning system":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :)))))")


print("Your final score:", score, "out of 3.")

if score >= 2:
    print("Good job! You're a quiz whiz!")
else: 
    print("Nice try! Better luck next time.")

print('Thanks for playing my game! I hope you enjoyed!')

