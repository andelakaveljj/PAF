import matplotlib.pyplot as plt
import numpy as np

F = float(input('Unesi iznos sile u N:'))
m = float(input('Unesi masu u kg:'))

a = F/m
d_t = 0.5
v=0
x=0
t=0
akceleracija=[]
brzina=[]
pomak=[]
vrijeme=[]

for i in range(20):
    v= v + a*d_t
    x = x + v*d_t
    t += d_t
    brzina.append(v)
    pomak.append(x)
    vrijeme.append(t)
    akceleracija.append(a)

plt.subplot(311) #prvi broj označava redove, drugi stupce, treći položaj
plt.plot(vrijeme,pomak)
plt.subplot(312)
plt.plot(vrijeme,brzina, 'r')
plt.subplot(313)
plt.plot(vrijeme,akceleracija, 'g')
plt.show()