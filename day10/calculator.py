from art import logo

#Add
def add(n1, n2):
    return n1 + n2

# Subtract
def substract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    num1 = float(input("What is your first number: "))

    should_continuer = True

    while should_continuer == True:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is your second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} :") == "y":
            num1 = answer    
        else: 
            should_continuer = False
            calculator()

calculator()