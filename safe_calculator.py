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
                return "Cannot divide by zero"
            return num1 / num2
        else:
            return f"Unsupported operation '{operation}'"

    except ValueError:
        return "Invalid number input"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
