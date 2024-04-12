import matplotlib.pyplot as plt
import numpy as np
import calculus as cls

def f2(x):
    return (x**2)   #definiram funkciju

koraci = []
gornje = []
donje = []
prosjecne = []

for i in range(100, 900, 100):
    a, b, c = cls.trapezna(f2, 0, 1, i)    #ne mogu razbit na tri linije koda radi return funkcije
    koraci.append(i)  #za svaki korak u for petlji dodajem u listu koraci
    donje.append(a)
    gornje.append(b)
    prosjecne.append(c)

plt.scatter(koraci, donje, c = "blue")
plt.scatter(koraci, gornje, c = "blue")
plt.scatter(koraci, prosjecne, c = "red")
plt.plot(koraci, prosjecne, c = "yellow")
plt.show()