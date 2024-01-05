def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
    }
def calculator():
    num1=int(input("What is the next number? "))
    for symbol in operations:
        print(symbol)
        
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation from the line above: ")
        num2=int(input("What is the next number? "))
        
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to exit: ").lower()=='y':
            num1=answer
        else:
            should_continue=False
            calculator()
        
calculator()
    
    
    
 