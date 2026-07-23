liste =[17, 38, 10, 25, 72]
print(liste)
liste.append(12)
print(liste)
liste = liste[::-1]
print(liste)
index = 0
for i in range(len(liste)):
    if(liste[i] == 17):
        index = i
        break

print(f"index de 17 = {index}")

liste = [i for i in liste if i != 38 ]
print(f"Liste sans l'élément 38 : {liste}")

print(f"sous liste de 2 eme au 3 eme : {liste[2:4]}")
print(f"sous liste de debut au 2 eme : {liste[:3]}")
print(f"sous liste du 3 eme à la fin : {liste[3:]}")

print(f"Le dernier élément est {liste[-1]}")
