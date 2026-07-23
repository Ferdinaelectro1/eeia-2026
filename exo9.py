entre = int(input("Entrez le nombre : "))
count = 1
old = 0
while old < entre:
    old = entre
    entre = int(input("Entrez le nombre : "))
    count += 1

print(count)    
