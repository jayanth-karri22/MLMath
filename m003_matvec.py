import numpy as np

mat = [[1,2], [2,3]]
transformation = [1,2]


M = np.array(mat)
v = np.array(transformation)

def mat_vec(a, b):
    sum = [0,0]
    for i in range(len(a)): 
         for j in range(len(b)):
              sum[i] += a[i][j] * b[j]

    return sum

print(mat_vec(mat, transformation))

assert mat_vec(mat, transformation) == list(M @ v)
assert mat_vec(mat, [1,0]) == [1, 2] 
assert mat_vec(mat, [0,1]) == [2, 3] 

print("matvec green tick")

