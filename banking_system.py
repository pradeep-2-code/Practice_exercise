accounts = {"alice": 1000, "bob": 500, "charlie": 750}


def show_menu():
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def check_balance(user):
    print(f"\n{user.title()}, your current balance is ₹{accounts[user]}")


def deposit_money(user):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            accounts[user] += amount
            print(f"₹{amount} deposited. New balance: ₹{accounts[user]}")
    except ValueError:
        print("Invalid input. Please enter a number.")


def withdraw_money(user):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > accounts[user]:
            print("Insufficient balance.")
        else:
            accounts[user] -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{accounts[user]}")
    except ValueError:
        print("Invalid input. Please enter a number.")


print("Welcome to Simple Bank!")

user = input("Enter your name: ").lower()

if user not in accounts:
    print("User not found. Exiting.")
else:
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit_money(user)
        elif choice == "3":
            withdraw_money(user)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")
