# Lesson 6 of Calculator Course


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


print("Simple Calculator App\n")  # Title
validOperators = ["+", "-", "/", "*"]

# While loop to keep app running
while True:
    try:
        # Grabbing user input
        firstNum = float(input("Input your first number: "))
        operator = str(input("Input operator: "))
        if operator not in validOperators:
            print("Invalid or unsupported operator, please try again\n")
            continue
        secondNum = float(input("Input your second number: "))
    except ValueError:
        print("Invalid input type, please try again\n")
        continue
    # Printing the result
    print("Result: {}\n".format(get_result(firstNum, secondNum, operator)))
