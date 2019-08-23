class First:
    x = 5


var1 = First()
print(var1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    variable = "random string"

    def greatMe(self):
        print("Hello, my name is: " + self.name)


p1 = Person("John", 32)
p2 = Person("Kate", 30)
print(p1.name + str(p1.age))
print(p2.name + str(p2.age) + p2.variable)
p1.greatMe()
p2.age = 31
print(p2.age)

