import re


def solve(s):
    x = re.findall("[0-9]+", s)
    for i in range(0, len(x)):
        x[i] = int(x[i])
    x.sort()
    return x[len(x) - 1]


print(solve("asfog14t94qnlfkgn2194nlakwng249t245fnbp"))
