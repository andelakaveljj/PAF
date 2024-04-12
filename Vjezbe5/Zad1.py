import matplotlib.pyplot as plt
import calculus as cls
import numpy as np

def f1(x):
    return x**3

cls.derivacija(f1, 2, 0.01)
a, b = cls.der(f1, -2, 2, 0.1)
c, d = cls.der(f1, -2, 2, 0.01)
plt.scatter(a, b, s = 2, c = "red")
plt.plot(c, d)
plt.show()