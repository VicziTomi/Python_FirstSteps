def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result


array_diff([3, 1, 2, 2, 3, 2, 1, 4, 1, 3, 4, 1, 5, 3], [1, 3])
array_diff([1, 2, 2], [2])
