import numpy  as np
import pandas as pd

np_arr = np.array([4,5,2,6])
print(np_arr)

print("\n")
np_2d_arr = np.array([[3,2],[6,2]])
print(np_2d_arr)

print("\n")
np_3d_arr = np.array([[[3,5],[8,1]],[[4,2],[5,6]]])
print(np_3d_arr)

print("\n")
ls = np.arange(0,3) #Des données de start à stop
print(ls)

print(f"Dimensions du tableau = {np_2d_arr.shape}")
print(f"Dimensions du tableau = {np_3d_arr.shape}")

rand_arr = np.random.randn(4,2) #Tableau 2d de 4 ligne et 2 colonne
print(rand_arr)

#les fonctions math de numpy
print("Sinus de numpy")
print(np.sin(rand_arr))

#Fonctions d'argréagations
print(f"somme de touts les ele du tableau = {rand_arr.sum()}") 
print(f"somme de touts les ele par lignes = {rand_arr.sum(axis=1)}") #1 line
print(f"somme de touts les ele par column = {rand_arr.sum(axis=0)}") #0 col 

t1 = np.array([1, 2, 3, 4, 5])
print(t1)
t2 = t1 + 2
print(t2)

print(np.hstack((t1, t2))) #ajoute le second t1 et t2, mais sur une seul ligne h = horizontal

print(np.vstack((t1, t2))) #ajoute sur colonne V = verticale

