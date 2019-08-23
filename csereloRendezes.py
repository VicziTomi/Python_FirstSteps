array = [36, 45, 67,  23, 53, 37, 49]
for i in range(0, len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
print(array)
