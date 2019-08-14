# Takes two numbers, num_1 and num_2 and
# returns the result of the operation specified by op.
#
# If op is not a supported operator, function will return "fail"
def get_result(num_1, num_2, op):
    if op == "+":
        return num_1 + num_2

    elif op == "-":
        return num_1 - num_2

    elif op == "*":
        return num_1 * num_2

    elif op == "/":
        return num_1 / num_2


print("Simple Calculator App")  # Title
# Grabbing user input
firstNum = float(input("Input your first number: "))
operator = input("Input operator: ")
secondNum = float(input("Input your second number: "))
# Printing the result
result = get_result(firstNum, secondNum, operator)
print("Result: {}".format(result))
