from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}


def perform_calculation():
    print(logo)
    go_again = True
    first_num = float(input("What's the first number?: "))
    while go_again:
        for key in operations:
            print(key)
        calculation_sym = input("Pick an operation: ")
        second_num = float(input("What's the second number?: "))
        answer = operations[calculation_sym](first_num, second_num)
        print(f"{first_num} {calculation_sym} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_num = answer
        else:
            go_again = False
            print("\n" * 20)
            perform_calculation()


perform_calculation()





