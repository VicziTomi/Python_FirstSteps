def largest_power(n):
    k = 0
    while 3 ** k <= n:
        k += 1
    return k - 1


print(largest_power(10))
