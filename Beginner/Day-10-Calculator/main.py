clear = lambda: os.system('cls')
from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    n1 = float(input("What's the first number?: "))
    for operator in operation:
        print(operator)
    shouldContinue = True

    while shouldContinue:
        operator = input("Pick an operation ")
        n2 = float(input("What's the next number?: "))

        calculation = operation[operator]
        answer = calculation(n1,n2)

        print(f"{n1} {operator} {n2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:
            shouldContinue = False
            calculator()

calculator()