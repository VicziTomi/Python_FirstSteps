class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)


x = Person("Jane", "Doe")
x.print_name()


class Student(Person):
    def __init__(self, first_name, last_name, year):
        Person.__init__(self, first_name, last_name)
        self.graduation_year = year

    def print_graduation(self):
        print("Year 'o: ", str(self.graduation_year))


y = Student("Gal", "Gadot", 2019)
y.print_name()
y.print_graduation()


class Lecturer(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)


z = Lecturer("Jake", "Taylor")
z.print_name()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

