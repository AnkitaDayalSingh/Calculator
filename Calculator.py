#Calculator

x = int(input("First Number: "))
op = input("Select Operator: ")
y = int(input("Second Number: "))

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

print(result)
