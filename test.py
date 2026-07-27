import timeit


def solution(heures: list, seuil: int):
    ctn = sum(1 for h in heures if h <= 0)
    return "NON" if ctn >= seuil else "OUI"
    
heures = []
seuil = -1

temps = timeit.timeit(lambda: solution(heures, seuil), number=100000)
print(f"Temps moyen par appel : {(temps/100000)*1e6:.3f} µs")