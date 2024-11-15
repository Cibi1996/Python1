from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1 / n2

calculator_dictionary ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# print(calculator_dictionary["*"](4,8))
def calculation():
    equal = "="
    n1 = float(input("What's the first number?: "))

    operation = input('''+
    -
    *
    /
    Pick an operation: ''')

    n2 = float(input("What's the second number?: "))

    n3 = calculator_dictionary[operation](n1, n2)


    print(f"{n1} {operation}{n2} {equal} {n3} ")
    stop = True
    while stop:
        choice = input(f"Type 'y' to continue calculating with {n3}, or type 'n' to start a new calculation:")
        choice = choice.upper()

        if choice == "Y":
            print(n3)
            n1 = n3
            n2 = int(input("What's the second number?: "))
            operation = input('''+
                -
                *
                /
                Pick an operation: ''')
            n3 = calculator_dictionary[operation](n1, n2)

            print(f"{n1} {operation}{n2} {equal} {n3} ")
        else:
            stop = False
            print("/n" * 20)
            print(logo)
            calculation()


calculation()