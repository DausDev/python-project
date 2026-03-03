name = input("Enter your name:")
height = float(input("Enter your HEIGHT :"))
while True:
    try:
        age = int(input("Enter your age :"))
        if age > 0 and age < 500:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid nu!")

print(f"Hello, {name}!")
print(f"You are {age} years old and {height} meters tall.")
