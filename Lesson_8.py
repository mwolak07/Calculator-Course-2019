# Lesson 8 of Calculator Course

from collections import deque


# Separates an input line using a list of separators
# Iterates over the input line character by character until an operator is found. At that point,
# the slice from the previous separator to the current one is appened to the output list,
# along with the current separator. After iteration is complete, the slice after the last operator is appended
# At every append operation, strip method is applied to get rid of whitespace
def separate_input(input_line, separators):
    output = []

    # Iterating over input line by index
    start = 0
    stop = 0
    while stop < len(input_line):
        # Checks to see if current character is operator
        if input_line[stop] in separators:
            # Appending proper terms
            output.append(input_line[start: stop].strip())
            output.append(input_line[stop].strip())
            # Incrementing counters
            stop += 1
            start = stop
        stop += 1

    # Appending final term
    output.append(input_line[start: stop + 1].strip())
    return output


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


# Checks to see if input is in order
# First makes sure input does not start or end with operator
# Then iterates through list and makes sure operators are not used multiple times back to back
def check_input_order(input_list, operators):
    # Starts or ends with operator
    if input_list[0] in operators or input_list[-1] in operators:
        return False

    # Scanning for repeat operators
    operator_flag = False
    for term in input_list:
        # Identified operator
        if term in operators:
            # Previous term was operator,
            if operator_flag:
                return False
            # Indicate operator was encountered
            else:
                operator_flag = True
        # Indicate term was not operator
        else:
            operator_flag = False

    return True


print("Simple Calculator App\n")  # Title
validOperators = ["+", "-", "/", "*"]

# While loop to keep app running
while True:
    # Getting user inputted expression string
    inString = input("Input your expression: ").strip()

    # Making sure start or end of input is not operator
    if inString[0] in validOperators or inString[-1] in validOperators:
        print("Expression cannot start or end with operator, please try again\n")
        continue

    # Separating terms of expression into a list
    inList = separate_input(inString, validOperators)

    # Making sure user inputted infix expression is correct
    if not check_input_order(inList, validOperators):
        print("Invalid input order, please try again\n")
        continue
    if not check_input_type(inList, validOperators):
        print("Invalid input type, please try again\n")
        continue

    print("Result: {}\n".format(evaluate_postfix(inList, validOperators)))
