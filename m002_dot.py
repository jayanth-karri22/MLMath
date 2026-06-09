import numpy as np

a = np.array([1,2])
b = np.array([3,4])

c = [1,2]
d = [3,4]

def dot_loop(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

def dot_vectorized(a,b):
    return np.sum(a * b)

assert dot_loop(a, b) == np.dot(a, b)
assert dot_vectorized(a, b) == np.dot(a, b)
assert dot_vectorized(np.array([0,2]), np.array([3,0])) == 0
print("green tick")