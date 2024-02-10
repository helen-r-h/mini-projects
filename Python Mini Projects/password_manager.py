pastor = input("What is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines(): # read lines of file called f
            data = line.rstrip()
            user, passw = data.split(" ") # looks for a space and creates a list with items and assigns to first element to user, 2nd element to passw
            print("User:", user, "Password:", passw)
def add():
    pass # LITERALLY PASS MEANS NOTHING
    name = input("Account Name: ")
    password = input("Password: ")
    # with will automatically close a file once your are done with it, before you had to open and close a file
    # modes: w, a, r 
    # w will clear previous file with same name and make a new one
    # r will just read file
    # a will add something to the end of a existing file, if file doesn't exist, will create a new one, if file does exist, will read file
    with open("passwords.txt", "a") as f: # f is file name
        f.write(name + " " + password + "\n") # writes in the file --> password.txt --> account name and then password


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add , press q to quit? ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()

    else: 
        print("Invalid mode. ")
        continue