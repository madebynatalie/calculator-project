from calculator.operations import calculate


def get_number(prompt):
    """
    Prompt the user for a number and validate input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """
    Main REPL loop for the calculator.
    """
    print("Welcome to the Command-Line Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.")

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print(
                "Invalid operation. Choose: add, subtract, multiply, or divide."
            )
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(operation, num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":  # pragma: no cover
    main()