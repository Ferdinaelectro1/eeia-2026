import pandas as pd

# Question 1 :Nettoyage des données  

unicef_df =  pd.read_csv("unicef_enfants.csv",encoding='cp1252',delimiter=";",
                         dtype={
                             "Annee" : "Int64"
                            }
                        )
print(unicef_df)

#Transformer les ages en numérique

print(unicef_df.info())
unicef_df["Avant_15"] = pd.to_numeric(unicef_df["Avant_15"],errors="coerce").astype("Int64")
unicef_df["Avant_18"] = pd.to_numeric(unicef_df["Avant_18"],errors="coerce").astype("Int64")
print(unicef_df.info())

#print(unicef_df[unicef_df.isna().any(axis=0)])

unicef_df = unicef_df.dropna(axis=0) #On supprime toutes les lignes contenant des données manquantes

print(unicef_df)
print(unicef_df.info())


#Question 2 : En 2018, dans quel pays y a-t-il eu le plus de filles mariées avant l’age 18 ans 

annee_2018_info = unicef_df[unicef_df["Annee"] == 2018]

print(annee_2018_info)

max_fille_avant_18 = annee_2018_info["Avant_18"].max()
print("Le pays concerné est : ")
print(annee_2018_info[annee_2018_info["Avant_18"] ==  max_fille_avant_18]["Pays"])

#Question 3 : nombre de filles mariées avant l’age de 18 ans représente plus de 5% du nombre total

total_filles = annee_2018_info["Avant_15"].sum() + annee_2018_info["Avant_18"].sum()
print(f"Total fille = {total_filles}")  

cinq_purcent_nbr_fille = int((0.05 * total_filles))
print(f"cinq_purcent_nbr_fille = {cinq_purcent_nbr_fille}")

print(annee_2018_info[annee_2018_info["Avant_18"] > cinq_purcent_nbr_fille].sort_values("Avant_18"))

#Question 4
unicef_df["Married_1"] = unicef_df["Avant_15"] != 0
print(unicef_df)



