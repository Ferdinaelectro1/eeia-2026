import numpy as np

A = np.arange(101)
B = np.array([102, 105, 10, 107, 7,106])

C = np.intersect1d(A,B)

print(C)
