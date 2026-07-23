ls = [14, 7, 6, 12, 2, 3, 3, 10]
print(ls)

ls[-1] = ls[-1] / 2
print(ls)

for i in range(len(ls)):
    ls[i] -= 1
print(ls)

for i in range(len(ls)):
    print(ls[i])

for i in range(len(ls)):
    if(ls[i] % 2 == 0):
        print(ls[i])

for i in range(len(ls)):
    str = ""
    for j in range(10):
       str += f"{ls[i]} "
    print(str)

for i in range(len(ls)):
    str = ""
    for j in range(int(ls[i])):
       str += f"{ls[i]} "
    print(str)

