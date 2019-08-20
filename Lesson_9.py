# Lesson 8 of Calculator Course

from queue import LifoQueue


def convert_infix(input_line):
    return ["beans"]


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


def evaluate_postfix(input_list, operators):
    stack = LifoQueue()

    for term in input_list:
        if term in operators:
            num1 = float(stack.get())
            num2 = float(stack.get())
            stack.put(get_result(num1, num2, term))
        else:
            stack.put(term)
    return float(stack.get())


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
    inList = input("Input your postfix expression: ").split(" ")

    if not check_input_type(inList, validOperators):
        print("Invalid input type, please try again\n")
        continue

    print("Result: {}\n".format(evaluate_postfix(inList, validOperators)))
