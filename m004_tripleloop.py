import numpy as np

mata = [[1,2], [3,4]]
matb = [[5,6], [7,8]]

A = np.array(mata)
B = np.array(matb)

def mat_mul( a,b):
    sum = [[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(b[i])):
                sum[i][j] += a[i][k]*b[k][j] 
    
    return sum

def mat_mul_dot(a,b):
    sum = [[0,0], [0,0]]
    for i in range(len(a)):
        for j in range(len(b)):
            sum[i][j] += np.dot(a[i], b[:,j])

    return sum


mat_mul(mata, matb)
mat_mul_dot(A, B)


ref = A @ B

assert np.array_equal(mat_mul(A, B), ref)
assert np.array_equal(mat_mul_dot(A,B), ref)



print(ref)