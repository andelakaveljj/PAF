import matplotlib.pyplot as plt
import numpy as np
import projectile as p

dts = [0.01,0.02,0.05]
for i in dts:
    pp=p.Projectile(1,0,0,10,0.2,0.2,0.2,45, i)
    x, y = pp.Euler()
    plt.scatter(x, y, s = 2)
ppp=p.Projectile(1, 0, 0, 10, 0.2, 0.2, 0.2,45,0.01)
x1,y1=ppp.Runge_Kutta()
plt.plot(x1,y1)
plt.show()