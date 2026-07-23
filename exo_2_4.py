def maximum(ls):
    maxi = 0
    for i in range(len(ls)):
        if(ls[i] > maxi):
            maxi = ls[i]
    return maxi

l = [2,6,9,1,0,3]
print(maximum(l))