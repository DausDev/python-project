# ATM Machine
# Show Balance
# Deposit Cash
# Withdraw Balance
# Exit

PIN = "1234"

def show_balance(balance):
    print(f"Current Balance: RM{balance:.2f}")

def deposit_cash():
    cash = float(input("Enter amount to deposit: RM"))

    if cash <= 0:
        print("Deposit must be more than RM0")
        return 0
    return cash

def withdraw_cash (balance):
    cash = float(input("Enter amount to withdraw: RM"))

    if cash <= 0:
        print("Withdrawal must be more than RM0")
        return 0
    if cash > balance:
        print("Insufficient balance")
        return 0

    return cash

attempts = 3
while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == PIN:
        print("PIN accepted. Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN {attempts} attempts remaining")

    if attempts == 0:
        print("Too many incorrect attempts. Card Blocked.")
        exit()

balance = 1000.00
choice = 0

print('Welcome to ATM Machine')

while choice != 4:
    print("\n1. Show Balance")
    print("2. Deposit Cash")
    print("3. Withdraw Cash")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_balance(balance)
    
    elif choice == 2:
        balance += deposit_cash()
        print(f"New Balance: RM{balance:.2f}")

    elif choice == 3:
        balance -= withdraw_cash(balance)
        print(f"New Balance: RM{balance:.2f}")

    elif choice == 4:
        print("Thx for using ATM Machine. Goodbye!")

    else:
        print("Invalid choice. Please try again.")
    # This is with the help of cGPT,Later I want to add, 
    # New Balance will be shown after each transaction.
  