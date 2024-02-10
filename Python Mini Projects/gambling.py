MAXLINES = 3

# collecting user input

def deposit():
    while True:
        lines = input("What would you like to deposit? $")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("lines must be greater than 0.")
                continue
        else:
            print("Please enter a valid number.")
            continue

    return lines 

def get_num_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 -" + str(MAXLINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINES:
                break
            else:
                print("Lines must be greater than 0.")
                continue
        else:
            print("Please enter a valid number.")
            continue

    return lines

def main():
    balance = deposit()
    liness = get_num_lines()



main()