import numpy as np

one_d_arr = np.random.randn(10)
print(one_d_arr)

one_d_arr_custom = np.random.normal(loc=10,scale=0.5,size=200000)
print(one_d_arr_custom)
print(f"Moyenne = {one_d_arr_custom.mean()}")


one_d_arr_custom_2 = np.random.randint(1,100,size=20)
print(one_d_arr_custom_2)

l = []
for p in range(2):
    l.append(list(np.random.uniform(0,1,5)))
one_d_arr_custom_3 = np.array(l)
print(one_d_arr_custom_3) 

one_d_arr_custom_4 = np.random.randint(1,100,(2,10))
print(one_d_arr_custom_4) 
