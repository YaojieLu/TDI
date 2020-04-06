
import numpy as np

cache = {}

# permutation evaluation
def f1(string):
    arr = [int(s) for s in string]
    arr = np.insert(arr, 0, 0)
    return np.abs(np.diff(arr)).sum()
def f2(string):
    arr = [int(s) for s in string]
    return np.abs(np.diff(arr)).sum()

# dynamic programming
def perm(s):
    key = str(s)
    res = []
    if len(s) == 1:
        return [s]
    if key in cache:
        return cache[key]
    else:
        for i, c in enumerate(s):
            for p in perm(s[:i] + s[i+1:]):
                res += [[c] + p]
    cache[key] = res
    return res
x = perm(list(range(1, 5)))
print(x)