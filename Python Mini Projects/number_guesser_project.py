import random # a module which is built into python which is your toolbox

secret_num = random.randrange(11) # (start, stop), generates a random number between start num and stop num, doesn't include stop num

print('Welcome to my number guesser game!')
user = input('Would you like to play? ')

if user.lower().strip() != "yes":
    print("Quit game.")
    quit()

print("Let's play!")

print('This is a number guesser game, and we have generated a random number. You will be given three tries to guess the number.')

guess_1 = int(input("Guess #1: "))
if guess_1 == secret_num:
    print("WOW! You got the number! Slay queen, luck is on your side today. ")
    print("Thanks for playing my game! Peace out!")
    quit()
else:
    print("Ooh. That's not right. You still have 2 tries!")
guess_2 = int(input("Guess #2: "))
if guess_2 == secret_num:
    print("Damn gurl. Sick guess, and you are correCTT!")
    print("Thanks for playing! Bye queen!")
    quit()
else:
    print("Tough luck, that is not right. But you still have one more try...")
guess_3 = int(input("Guess #3: "))
if guess_3 == secret_num:
    print("AANND the queen saves it! BOOM! Last try, and you got it! Slayful and timely!")
    print("Thanks for playing. Have a FANTAstic day!")
    quit()
else:
    print("OOF! No luck in your hands today. But at least you tried!")
    print("The number was", secret_num, ".")
    print("Thanks for playing! See ya!")
    quit()
