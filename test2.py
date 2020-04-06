
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
    res = []
    if len(s) == 1:
        return [s]
    if s in cache:
        return cache[s]
    else:
        for i, c in enumerate(s):
            for p in perm(s[:i] + s[i+1:]):
                res += [c + p]
    cache[s] = res
    return res
print(perm('123456789o'))