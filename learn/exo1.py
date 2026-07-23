import numpy as np
import pandas as pd
"""

"""

ventes = {
    'Produit': ['Clavier', 'Souris', 'Ecran', 'Clavier', 'Souris', 'Ecran'],
    'Prix_Unitaire': [25, 15, 150, 25, 15, 150],
    'Quantite': [4, 10, 2, 6, 8, 1],
    'Categorie': ['Info', 'Info', 'Tech', 'Info', 'Info', 'Tech']
}

df_ventes =  pd.DataFrame(ventes)

print(df_ventes)
df_ventes["Total"] = df_ventes['Prix_Unitaire'] * df_ventes["Quantite"]
print(df_ventes)

print("Ventes dont le prix est supérieur à 100 euro")
print(df_ventes[df_ventes['Total'] >= 100])

print(f"Total des ventes = {df_ventes["Total"].sum()}")

print("\nTotal des ventes par catégorie :")
print(df_ventes.groupby('Categorie')['Total'].sum())

print("\n")
arr = np.random.randn(3, 4)
print(arr)
a1 = arr.shape
print(a1)
a2 = arr.reshape(1, 12)
print(a2)