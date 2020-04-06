from itertools import permutations
import numpy as np

def f(N):
    sum1, sum2 = 0, 0
    for perm in permutations(list(range(1, N+1)), N):
        arr = np.insert(np.asarray(perm), 0, 0)
        x = np.abs(np.diff(arr)).sum()
        sum1 += x
        sum2 += x**2 
    total = np.math.factorial(N)
    return np.sqrt(sum2/total-(sum1/total)**2)

print(f(10))