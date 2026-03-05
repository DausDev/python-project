# def greet_person(name):
#     print(f"Hello, {name}!") #This function takes a name as an argument and prints a greeting message using an f-string for formatting.
# greet_person("Alice")

# def add_numbers(a, b): #This function takes two arguments and returns their sum.
#     return a + b

# result = add_numbers(5, 3)
# print(result)

# def greet_with_title(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Smith"))
# print(greet_with_title("Johnson", "Dr."))

# def sum_all(*args): 
#     return sum(args) #*args allows for a variable number of arguments to be passed to the function, and sum() calculates their total.

# print(sum_all(1,2,3,4,5)) 

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}") #This function takes a dictionary as an argument and prints its key-value pairs using an f-string for formatting.
        
# print_info(name="Alice", age=25, city="New York")

# def flexible_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function(1, 2, 3, name="Alice", age=25)

# square = lambda x: x**2 #This line defines a lambda function that takes a single argument x and returns its square. Lambda functions are anonymous functions that can be defined in a single line.
# print(square(4))

# minus = lambda x, y: x - y
# print(minus(2026, 1986))

# square_root = lambda x: x **0.5
# print(square_root(25))

# def prime_numbers(n):#This function takes a number n as an argument and returns a list of all prime numbers up to n. It uses a nested loop to check if each number is prime by testing divisibility against all numbers up to its square root.
#     primes = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for divisor in range(2, int(num**0.5) + 1):
#             if num % divisor == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
# print(prime_numbers(20))

# calculate_total(price, quantity) #This function takes two arguments, price and quantity, and returns the total cost by multiplying them together.
# def calculate_total(price, quantity):
#     return price * quantity

# total_cost = calculate_total(19.99, 3)
# print(total_cost)

def total_amps(voltage, resistance): #This function calculates the total current (in amps) using Ohm's Law, which states that current (I) is equal to voltage (V) divided by resistance (R).
    return voltage / resistance
voltage = 240
resistance = 24
current = total_amps(voltage, resistance)
print(f"The total current is: {current} amps")

def celcius_to_fahrenheit(celcius):
    input("Enter the temperature in Celcius: ")
    return (celcius * 9/5) + 32

celcius = 100
print(f"{celcius} degrees Celsius is equal to {celcius_to_fahrenheit(celcius)} degrees Fahrenheit.")