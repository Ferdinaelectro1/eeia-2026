import numpy as np

arr = np.array([
    [4  ,  2      , np.nan] ,
    [8  ,  np.nan , 56 ],
    [23 ,  12     , 89]
])

print(arr)

arr[np.isnan(arr)] = 2026

print(arr)