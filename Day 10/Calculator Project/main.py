import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    first_num = int(input("What's the first number?: "))
    keep_going = True

    while keep_going:
        for char in operations:
            print(char)
        input_operation = input(f"Choose an operation: ")
        second_num = int(input("What's the second  number?: "))
        result = operations[input_operation](n1= first_num, n2= second_num)
        print(result)
        ask_again = input("Do you want to continue? (y/n): ")
        if ask_again == "y":
            first_num = result
        else:
            keep_going = False
            print("\n" * 20)
            calculator()

calculator()