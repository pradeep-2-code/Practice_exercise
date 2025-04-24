x = int(input("Enter the year"))
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print("Its a leap year")
else:
    print("Its not a leap year")
