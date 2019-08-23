import random

if 5 > 2:
    print("5 is greater than two")
x = "Cuki"
y = "Cicn"
z = x + " " + y
# print(z)

a = 2j
# print(type(a))
# print(a)

tenthPow = 1e6
# print(tenthPow)

# Generate random number:
minValue = 1355425
maxValue = 245135777235
genNumber = random.randrange(minValue, maxValue)
print(genNumber)
print(random.randrange(0, 1000))

b = "this is a random string"
print(b.replace("s", "x"))

fruits = ["Pear", "Melon", "Kiwi"]
fruits.append("cherry")
print(fruits)

gyumi = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

print(len(gyumi))
gyumi.update(more_fruits)
gyumi.pop()
print(gyumi)
print(len(gyumi))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(str(x) + ": " + str(y))


def firstfunc(n):
    return lambda a: a * n


mydoubler = firstfunc(2)
print(mydoubler(23))

newarr = [42, 57, 32, 24, 55, 24]
newarr.sort()
newarr.reverse()
print(newarr)

