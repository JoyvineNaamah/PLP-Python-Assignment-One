# Getting the inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the mathematical operation (+, -, *, or /): ")

# Performing the operation based on the user's input
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

# Printing the result
print(f"{num1} {operator} {num2} = {result}")