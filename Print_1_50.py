# •	Write a Python program that prints numbers from 1 to 50 but:
# o	Replaces multiples of 3 with "Fizz".
# o	Replaces multiples of 5 with "Buzz".
# o	Replaces multiples of both 3 and 5 with "FizzBuzz".

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
