import random
import time

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBS = 10


# generating problem 
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer
    
wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

# problems and getting wrong
for i in range(TOTAL_PROBS):
    expression, answer = generate_problem()
    while True:
        ans = input("Problem # " + str(i + 1) + ": " + expression + " = ")
        if ans == str(answer):
            break
        print("Try again, wrong.")
        wrong += 1

end_time = time.time()
total_t = int(end_time - start_time)

print("---------------------")
print("Nice work, you finished in: " + str(total_t) + " seconds.")