def friend(x):
    fin = []
    for name in x:
        if len(name) == 4:
            fin.append(name)
    return fin


print(friend(["Ryan", "Kieran", "Mark"]))

x = "This is to be splitted by whitespace"
print(x.split())


def expanded_form(num):
    num_format = str(num)
    fin = ""
    decimal = len(num_format) - 1
    for char in num_format:
        if char != "0":
            fin += char + decimal * "0" + " + "
        decimal -= 1
    return fin[0:len(fin) - 3]


expanded_form(70304)


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    countN = 0
    countW = 0
    countS = 0
    countE = 0
    for i in walk:
        if i == "n":
            countN += 1
        elif i == "w":
            countW += 1
        elif i == "s":
            countS += 1
        else:
            countE += 1
    print(countN, countW, countS, countE)
    if countN != countS or countE != countW:
        return False
    return True


print(is_valid_walk(["n", "e", "e", "s", "w", "w", "n", "n", "s", "s"]))
print(is_valid_walk(["n", "s", "n", "w", "n", "s", "e", "s", "n", "s"]))

