import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x/(1 + x**3)

T = np.linspace(0, 5, 2000)
print(T)
Y = f(T)
plt.plot(T, Y)
plt.title(r'Courbe de $\frac{x}{1 + x^3}$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.savefig("imp.png")
plt.show()
