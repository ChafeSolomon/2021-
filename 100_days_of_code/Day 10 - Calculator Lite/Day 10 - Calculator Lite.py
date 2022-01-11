import art
#Calculator
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
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    #Here we select "+"
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    calculate_again = "y"
    while calculate_again == "y":
    #Here we select "*" which overides the "+" we selected on line 26.
        operation_symbol = input("Pick an operation: ") 
        num3 = float(input("What's the next number?: "))

        #Here the calculation_function selected will be the multiply() function
        calculation_function = operations[operation_symbol] 

        second_answer = calculation_function(first_answer, num3)
        #In the next lesson, we will delete all the code from line 34-48 so don't worry
    #It won't affect your final project.
    #But it's a good oportunity to practice debugging. 🐞

        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

        calculate_again = input("Would you like to calculate again: y or n?")
        if calculate_again == "y":
            first_answer = second_answer
        else:
            print("")
            calculator()
calculator()
