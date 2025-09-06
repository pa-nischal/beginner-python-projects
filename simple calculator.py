# This is a simple calculator which lets the user add, subtract, multipy and divide using two numbers.

operator = input("Enter a mathematical operator(+ - * /):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    if num2 == 0:
        answer="Infinite"
    else:
        answer = num1 / num2
else:
    print("This operator is not supported.")

print(f"Answer: {answer}")
input("Press any button to exit...")