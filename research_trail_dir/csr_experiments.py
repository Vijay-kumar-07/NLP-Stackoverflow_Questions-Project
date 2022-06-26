import numpy as np
from scipy.sparse import csr_matrix

A = np.array([
    [1,0,0,0,0,1,0],
    [3,0,0,2,4,1,2],
    [0,0,0,0,0,1,0]
])

S = csr_matrix(A)
print(S)

B = S.todense()
print(B)