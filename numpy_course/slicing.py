import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[1:4])
print(a[::2])
print(a[::-1])

print("\n")
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print("\n")
print(b[0, :]) # 1ère ligne entière
print("\n")
print(b[:, 1]) # 2e colonne entière
print("\n")
print(b[1:3, 1:]) # sous-matrice
print("\n")
print(b[::-1, :]) # inverse les lignes