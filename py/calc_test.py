# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     result = num1 + num2
#     print(f"The sum of {num1} and {num2} is: {result}")
# except ValueError:
#     print("Please enter valid numbers!")
# print(result)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Performing integer division...")
    result = num1 // num2
    print(f"The division of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid numbers!")
print(result)