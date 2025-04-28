accounts = {"alice": 1000, "bob": 500, "charlie": 750}


def show_menu():
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")


def checking_balance(user):
    for k, v in accounts.items():
        if user == k:
            balance = v
    return balance


def depositing_money(user):
    for k, v in accounts.items():
        if user == k:
            dep = int(input("Enter the amount you want to deposit"))
            v += dep
            net_balance = v
    return net_balance


def withdrawing_money(user):
    for k, v in accounts.items():
        if user == k:
            wid = int(input("enter the amount you want to withdraw"))
            v = v - wid
            if v < 0:
                print("You do not have enough balance")
            else:
                print(v)


print("welcome to the bank")
user = input("enter your user name").lower()

if user in accounts.keys():
    print(show_menu())
    a = int(
        input(
            "Select any one option out of \n 1.checking balance \n2.depositing money \n3.withdrawing money"
        )
    )
    if a == 1:
        print("The balance in your account is :", checking_balance(user))
    elif a == 2:
        print("Your net balance after depositing is :", depositing_money(user))
    elif a == 3:
        print(withdrawing_money(user))
    else:
        print("Invalid Choice")
else:
    print("Please enter correct username")
