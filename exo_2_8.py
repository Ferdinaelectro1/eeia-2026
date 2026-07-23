def compterMots(er : str):
    d = {}
    word = ""
    for c in er:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(compterMots("anticonstitutionnellement"))
