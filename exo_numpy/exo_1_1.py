import numpy as np

u = np.array([1, 2, 3])
v = np.array([5,6, 7])

print(f"Le produit scalaire donne : {np.dot(u,v)}")
print(f"Le produit scalaire donne : {(u*v).sum()}")


