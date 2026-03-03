try:
    number = float(input("Enter a Number: "))
    if number > 0:
            print("The number is positive.")
    elif number <0:
            print("The number is negative.")
    else:
            print("The number is zero.")
            
    print (number / 100) 
    print("This is the end of the program.")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")