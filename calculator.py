print("this is a basic command line calculator...")
print("gimme a number")
x = input()
try:
    x_int = int(x)
except ValueError:
    print("Not a number")
    exit()
print("gimme another")
y = input()
try:
    y_int = int(y)
except ValueError:
    print("Not a number")
    exit()
operations = {"addition": 1, "subtraction": 2, "multiplication": 3, "division": 4}
print("what do you wanna do?")
for x in operations:
    print(str(operations[x]) + " " + x)
print("use the corresponding number code to operate on given numbers")
op = int(input())
if op == 1:
    print("Result is: " + str(x_int + y_int))
elif op == 2:
    print("Result is: " + str(x_int - y_int))
elif op == 3:
    print("Result is: " + str(x_int * y_int))
elif op == 4:
    print("Result is: " + str(float(x_int / y_int)))
