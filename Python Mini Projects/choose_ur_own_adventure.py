name = input("Your name: ")
print("Welcome", name + "!")

input = input("You have 2 paths, left or right?")

if input.lower().strip() == "left":
    a1 = input("Ok, you can either go to a blue castle or the green mountains, choose one. ")

    if a1.lower().strip() == "blue castle":
        print("The blue castle is decorated with golden seashells, glimmering with pearls and merwomen swim around the castle. Do you want to enter the castle or talk to one of the merwomen?")

    if a1.lower().strip() == "green mountains":
        print("Smoke wafts into your nose as you approach the mountain, and you hear gasps and chatter in the deeper in the mountain, do you go towards the sound or move on?")
        
elif input.lower().strip() == "right":
    a1 = input("Ok, you have come to the city of Parisle, you can either enter the city or continue your journey. ")
else: 
    print("Not valid, YOU LOSE!!!!!")