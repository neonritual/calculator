from art import logo

#Calculator

def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  print(logo)
  will_continue = True
  answer = ''

  while will_continue == True:
    if not answer:
      num1 = float(input("What's the first number? "))
      num2 = float(input("What's the second number? "))
      for symbols in operations:
        print(symbols)  
      operation_symbol = input("Pick an operation symbol from the line above. ")
      operation = operations[operation_symbol]
      answer = operation(num1, num2) 
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    else:
      num_next = int(input("What's the next number? "))
      for symbols in operations:
        print(symbols)
      operation_symbol = input("Pick an operation symbol from the line above. ")
      operation = operations[operation_symbol]
      old_answer = answer
      answer = int(operation(answer, num_next))
      print(f"{old_answer} {operation_symbol} {num_next} = {answer}")
    want_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to begin a new calculation. ")
    if want_continue == "n": 
      will_continue = False
      calculator()
      

calculator()









# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?"))
# operation = operations[operation_symbol]
# second_answer = operation(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


