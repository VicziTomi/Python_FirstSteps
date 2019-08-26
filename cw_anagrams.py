def anagrams(word, words):
    res = []
    x = [char for char in word]
    x.sort()
    for w in words:
        temp = [char for char in w]
        temp.sort()
        if temp == x:
            res.append(w)
    return res


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

