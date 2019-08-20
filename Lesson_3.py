# Lesson 3 of Calculator Course

print("Simple Calculator App\n")  # Title
# Grabbing user input
firstNum = float(input("Input your first number: "))
operator = str(input("Input operator: "))
secondNum = float(input("Input your second number: "))

if operator == "+":
    answer = firstNum + secondNum
    print("Result: {}".format(answer))

elif operator == "-":
    answer = firstNum - secondNum
    print("Result: {}".format(answer))

elif operator == "*":
    answer = firstNum * secondNum
    print("Result: {}".format(answer))

elif operator == "/":
    answer = firstNum / secondNum
    print("Result: {}".format(answer))
