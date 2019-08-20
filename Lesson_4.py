# Lesson 4 of Calculator Course


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
# Grabbing user input
firstNum = float(input("Input your first number: "))
operator = str(input("Input operator: "))
secondNum = float(input("Input your second number: "))
# Printing the result
result = get_result(firstNum, secondNum, operator)
print("Result: {}".format(result))
