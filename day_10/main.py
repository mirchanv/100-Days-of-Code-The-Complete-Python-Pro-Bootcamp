from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        for symbol in math_operations:
            print(symbol)
            
        picked_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = math_operations[picked_operation](num1, num2)
        print(f"{num1} {picked_operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'q' to quit the application: ").lower()

        if choice == "q":
            print("Application ended successfully!")
            exit()
        elif choice == "y":
            num1 = result
        else:
            print("\n" * 20)
            calculator()

calculator()







