from functools import reduce
from itertools import groupby
import re


def product(numbers):
    result = 1
    if len(numbers) == 0:
        return None
    elif numbers is None:
        return None
    else:
        for i in numbers:
            result *= i
    return result


# print(product([5, 4, 1, 3, 9]))


def even_numbers_before_fixed(sequence, fixed_element):
    if fixed_element not in sequence:
        return -1
    evens = list(filter(lambda x: x % 2 == 0, sequence))
    print(evens)
    if len(evens) == 0:
        return 0


# print(even_numbers_before_fixed([1, 4, 2, 6, 3, 1], 6))
# print(even_numbers_before_fixed([2, 3, 4, 3], 3))


def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 1
    actual = 0
    while actual <= desiredHeight:
        actual += upSpeed
        if actual >= desiredHeight:
            break
        actual -= downSpeed
        if actual >= desiredHeight:
            break
        days += 1
    return days


# print(growing_plant(100, 10, 910))
# print(growing_plant(10, 9, 4))


def scoreboard(string):
    x = str.split(string, " ")
    res = []
    dictionary = {"nil": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                  "nine": 9}
    for i in x:
        if i in dictionary:
            res.append(dictionary[i])
    return res


# print(scoreboard("epnh qprng qwpn 24 qpwnrg, six qwkgn4+++ two"))


def odd_one(arr):
    ind = 0
    for i in arr:
        if i % 2 != 0:
            ind = arr.index(i)
    if ind > 0:
        return ind
    else:
        return -1


# print(odd_one([2, 4, 6, 7, 10]))

def solution(number):
    divisors = []
    for i in range(1, number):
        if i % 3 == 0:
            divisors.append(i)
        elif i % 5 == 0:
            divisors.append(i)
    return reduce(lambda a, b: a + b, divisors)


# print(solution(50))

def digital_root(n):
    t = 0
    while n > 9:
        t = 0
        temp = str(n)
        for j in range(len(temp)):
            t += int(temp[j])
        n = t
    return t


# print(digital_root(493193))

def move_zeros(array):
    res = []
    for i in array:
        if i != 0 or i is False:
            res.append(i)
    for x in range(len(res), len(array)):
        res.append(0)
    return res


# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))

def unique_in_order(iterable):
    x = list(iterable)
    x.append("x")
    x.append("x")
    res = []
    for i in range(0, len(x) - 1):
        if x[i] != x[i + 1]:
            res.append(x[i])
    return res


# print(unique_in_order("AAAABBBCCDAABBB"))

def unique(iterable):
    return [k for (k, _) in groupby(iterable)]


# print(unique("AAAABBBCCDAABBB"))

def order(sentence):
    x = sentence.split(' ')
    res = x.copy()
    for c in x:
        val = re.findall(r'\d', c)
        ind = int(val[0]) - 1
        res[ind] = c
    return " ".join(res)


# print(order("is2 Thi1s T4est 3a"))

def alphabet_position(text):
    lo = text.lower()
    res = []
    for i in range(0, len(lo)):
        if lo[i].isalpha():
            res.append(change_char(lo[i]))
    return "".join(str(res).strip('[]').replace(",", ""))


def change_char(a):
    alp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
           'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
           'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    return alp.get(a)


# print(alphabet_position("The sunset sets at twelve o' clock."))

def iq_test(numbers):
    arr = numbers.split(" ")
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    if arr[0] % 2 == 0:
        return int(a.index(False, 0, len(arr)) + 1)
    if arr[0] % 2 != 0:
        return int(b.index(True, 0, len(arr)) + 1)


print(iq_test("2 4 7 8 10"))
print(iq_test('1 2 2'))
