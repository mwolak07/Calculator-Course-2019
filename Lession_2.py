# Grabbing the first number
print("Simple Calculator App")

firstNum = int(input("Input your first number: "))
operator = input("Input operator: ")
secondNum = int(input("Input your second number: "))

if operator == "+":
    answer = firstNum + secondNum
    print(answer)

elif operator == "-":
    answer = firstNum - secondNum
    print(answer)

elif operator == "*":
    answer = firstNum * secondNum
    print(answer)

elif operator == "/":
    answer = firstNum / secondNum
    print(answer)
