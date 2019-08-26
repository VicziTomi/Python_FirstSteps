def score(dice):
    ones = dice.count(1)
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    sixes = dice.count(6)
    result = 0
    if twos == 3:
        result += 200
    if threes == 3:
        result += 300
    if fours == 3:
        result += 400
    if sixes == 3:
        result += 600
    if ones >= 3:
        result += 1000 + (5 - ones) * 100
    else:
        result += ones * 100
    if fives >= 3:
        result += 500 + (5 - fives) * 50
    else:
        result += fives * 50
    return result


print(score([2, 4, 4, 5, 4]))
