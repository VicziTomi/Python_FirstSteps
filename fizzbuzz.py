minValue = 1
maxValue = 100
for v in range(minValue, maxValue):
    if v % 3 == 0 and v % 5 == 0:
        print("FizzBuzz")
    elif v % 3 == 0:
        print("Fizz")
    elif v % 5 == 0:
        print("Buzz")
    else:
        print(v)


#TODO
#implement Fibonacci and prime number checker implementation
