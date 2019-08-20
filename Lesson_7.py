# Lesson 7 of Calculator Course

from queue import LifoQueue


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
