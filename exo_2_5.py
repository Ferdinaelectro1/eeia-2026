def maximum_index(ls):
    maxi  = 0
    index = 0
    for i in range(len(ls)):
        if(ls[i] > maxi):
            maxi = ls[i]
            index = i
    return index

l = [2,6,9,1,0,3]
print(maximum_index(l))