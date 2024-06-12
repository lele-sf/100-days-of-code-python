from art import logo


def calculate(num_one, num_two, operation):
    if operation == "+":
        result = num_one + num_two
    elif operation == "-":
        result = num_one - num_two
    elif operation == "*":
        result = num_one * num_two
    elif operation == "/":
        if num_two == 0:
            return "Error: Division by zero is undefined."
        result = num_one / num_two
    return result


continue_calc = 'y'
print(logo)
num_one = float(input("What's the first number?: "))

while continue_calc == 'y':
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please try again.")
        continue
    num_two = float(input("What's the next number?: "))
    result = calculate(num_one, num_two, operation)
    print(f"{num_one} {operation} {num_two} = {result}")
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continue_calc == 'y':
        num_one = result
