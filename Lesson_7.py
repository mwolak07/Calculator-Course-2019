# Lesson 7 of Calculator Course

from collections import deque


# Takes two numbers, num_1 and num_2 and
# returns the result of the operation specified by op.
def get_result(num_1, num_2, op):
    if op == "+":
        return num_1 + num_2

    elif op == "-":
        return num_1 - num_2

    elif op == "*":
        return num_1 * num_2

    elif op == "/":
        return num_1 / num_2


# Evaluates a postfix expression using a stack
# Scans through input, left to right. If term is a number, it is pushed onto the stack.
# If it is an operator, the last two numbers are popped off of the stack,
# and the result of the operation with those two numbers it pushed onto the stack.
# At the end, the last thing on the stack is the result, which is popped and returned
def evaluate_postfix(input_list, operators):
    stack = deque()

    # Iterating through input
    for term in input_list:
        # Performing operation for operator term
        if term in operators:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            stack.append(get_result(num1, num2, term))
        # Pushing to stack for number
        else:
            stack.append(term)

    # Returning last thing on the stack
    return float(stack.pop())


# Checks to see if input types are valid (float) by trying to cast every term except for operators to a float.
# If this raises a ValueError, the type was wrong, and input must be re-entered
def check_input_type(input_list, operators):
    # Iterating through terms in input
    for term in input_list:
        # Attempting to cast term to float (unless it is an operator)
        try:
            if term in operators:
                continue
            float(term)

        except ValueError:
            return False

    return True


print("Simple Calculator App\n")  # Title
validOperators = ["+", "-", "/", "*"]

# While loop to keep app running
while True:
    # Getting user inputted postfix expression
    inString = input("Input your postfix expression: ").strip()

    # Splitting user input into terms using spaces
    inList = inString.split(" ")

    # Making sure input type is valid
    if not check_input_type(inList, validOperators):
        print("Invalid input type, please try again\n")
        continue

    print("Result: {}\n".format(evaluate_postfix(inList, validOperators)))
