import numpy as np

Pierre = np.array([100, 90, 95, 100, 80])
Codjo = np.array([101, 90,96, 95, 80])

b = (Pierre == Codjo)
week_days = np.array(["Lundi","Mardi","Mercredi","Jeudi","Vendredi"])

print(f"Les jours où la collecte est identique sont:  {week_days[b]}")