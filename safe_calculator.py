def safe_calculator(operation, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        else:
            return f"Error: Unsupported operation '{operation}'"

    except ValueError:
        return "Error: Invalid number input"
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}"
