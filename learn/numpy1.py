import numpy  as np
import pandas as pd 

ma_liste = [5, 10, 15, 20, 25]

arr = np.array(ma_liste)

print(f"Arr*2 = {arr*2}")

masque = arr > 15
print(f"Masque = {masque}")
print(f"Tableau > 15 = {arr[masque]}")

notes = np.array([12, 8, 15, 6, 18, 9, 14])
reussite = notes >= 10
print(notes[reussite])

print("------------\n")
donnees = {
    'Nom': ['Chado', 'Lea', 'Richard', 'Bedo'],
    'Age': [14, 23, 26, 43],
    'ville' : ["Ouake","Lokossa","Calavi","Ouake"]
}
df = pd.DataFrame(donnees)
print(df)
print("\n------------")
print(df["ville"])
print(df[df['Age'] >= 20])
df["statut"] = "Etudiant"
print(df)
df["Age+5"] = df["Age"]+5
print(df)
df["Majeur"] = df["Age"] >= 18
print(df)
df["Annee_Naissance"] = 2026 - df["Age"]
print(df)

print(df.groupby("ville")["Age"].mean())
print(df.groupby("ville")["Age"].count())