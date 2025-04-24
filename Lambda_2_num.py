# Implement a lambda function that:
# Takes two numbers as input.
# Returns their product if both are even, otherwise their sum.

function = (
    lambda num1, num2: num1 * num2 if (num1 % 2 == 0 and num2 % 2 == 0) else num1 + num2
)
print(function(17, 20))
