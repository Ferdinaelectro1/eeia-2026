import numpy as np

a = np.array([[1 , 2, 6, 4], [5, 4, 7, 11], [9, 10, 8, 12]])
print(a)
condition1 = a < 5
print(condition1)
print(a[condition1])
gt_5 = (a >= 5)
print(gt_5)
print(a[gt_5])
divisible_par_2 = a[a%2==0]
print(divisible_par_2)