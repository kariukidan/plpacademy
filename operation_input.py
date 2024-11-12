# Get user input for two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

#  calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
else:
    print("Invalid operator")

# Print the result
print(f"{num1} {operator} {num2} = {result}")