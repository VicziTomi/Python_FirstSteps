print("Tomi")
print(32)
shopList = ["Apple", "Cherry", "Mango"]
print(shopList)
shopList.append("Pear")
print(shopList)
del shopList[1]
shopList.remove("Apple")
print(shopList)
print(len(shopList))

students = {"Abc": 12, "Def": 15, "Ghi": 16}
print(students)
print(students["Abc"])

for x in students:
    print(x)

for x in shopList:
    print(x)

if "Mango" in shopList:
    print("correct")

anotherList = ["item", "bag", "foo"]
anotherList.pop()
print(anotherList)
x = y = "konfuise"
y = "alternate"
print(y)

anotherList.append(x if x is y else "diszkonfuz")
print(anotherList)

thisset = {"alma", "banan"}
thisset.update(["citrom", "dinnye"])
print(thisset)

