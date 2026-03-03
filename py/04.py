# score = int(input("Enter your score: "))

# score = int(score)
# if score >= 90:
#         print("Grade: A")
# elif score >= 80:
#         print("Grade: B")
# elif score >= 70:
#         print("Grade: C")
# elif score >= 60:
#         print("Grade: D")
# else:
#         print("Grade: F")

# user_age = int(input("Enter your age: "))
# has_licence = input("Do you have a driving licence? (yes/no): ").lower()
# if user_age >= 18 and user_age < 60 and has_licence in ["yes", "y"]:
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")

# day = input ("What day is it in the week?  =")
# if day == "Saturday" or day == "Sunday":
#     print("It's a weekend.")
# else:
#     print("It's a weekday.")

height = float(input("Enter your HEIGHT (meters) :"))
weight = float(input("Enter your WEIGHT (kilograms) :"))
BMI = weight / (height ** 2)

if BMI < 18.5:
    print("Underweight")
elif BMI < 24.9:
    print("Normal weight")
elif BMI < 29.9:
    print("Overweight")
else:
    print("Obese")