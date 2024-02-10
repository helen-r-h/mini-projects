# set up phone book - empty dict to store shit
phonebook = {} 

# getting user input

while True:
    print("\nWelcome to the phonebook app!")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

     # ask user what they want to do

    # checking user input
    while True:
        choice = input("Select an option: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= 4:
                break
            else:
                print("The number must be greater than 0 and less or equal to 4.")
                continue
        else: 
            print("Please input a valid number.")
            continue

    # which choice?

    if choice == 1:
        name = input("Enter name: ")
        phone_num = input("Enter phone number: ")
        phonebook[name] = phone_num
        print("Contact added successfully!")
    if choice == 2:
        print("Contacts: ")
        for name, phone_num in phonebook.items():
            print(f"{name}: {phone_num}")

    if choice == 3: 
        name = input("Contact Name: ")
        if name in phonebook:
            phone_num = phonebook[name]
            print(f"{name}: {phone_num}")
        else:
            print("Contact not found.")

    if choice == 4:
        print("Exiting Phonebook.")
        break

