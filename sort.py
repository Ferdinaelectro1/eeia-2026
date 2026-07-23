def tri(ls: list):
    size= len(ls)
    for i in range(len(ls)):
        for j in range(i,len(ls)):
            if ls[i] > ls[j]:
                temp    = ls[j]
                ls[j] = ls[i]
                ls[i]   = temp

    return ls

print(tri([2,1,7,3,9,45,23,87,123,12,0]))

