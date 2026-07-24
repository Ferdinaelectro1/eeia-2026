import numpy as np

matrice = np.random.randn(5,10)
print(matrice)
print("Moyenne de chaque ligne")
print(matrice.mean(axis=1))

# lmoy = []
# for i in range(5):
#     lmoy.append(matrice[i].mean())

# moy = np.array(lmoy)
# print(moy)