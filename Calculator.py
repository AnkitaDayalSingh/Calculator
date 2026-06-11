#Calculator

def operation(x, y, op):
    if op == '+':
        result = x + y
    elif op == "-":
        result = x - y
    elif op in ["*", "×"]:
        result = x * y
    elif op in ["/", "÷"]:
        if y == 0:
            result = "Can not divide by zero"
        else:
            result = x / y
    elif op in ["^","**"]:
        result = x**y
    else:
        result = "Invalid Operator"
    return result

while True:
    print("1 New Calculation")
    print("0 Exit")
    a = int(input("Enter: "))

    if a == 1:
        x = int(input("First Number: "))
        op = input("Select Operator: ")
        y = int(input("Second Number: "))
        
        output = operation(x, y, op)
        print(output)
    
    elif a == 0:
        break
    else:
        print("Invalid Input")
        continue
