import matplotlib.pyplot as plt
from math import sin, cos

v0=float(input('Unesi iznos početne brzine:'))
theta=float(input('Unesi iznos kuta otklona:'))

vx=v0*cos(theta)
vy=v0*sin(theta)
y=0
x=0
t=0
dt=0.1
g=9.81
pomak_x=[]
pomak_y=[]
vrijeme=[]

for i in range(100):
    x = x + vx*dt
    vy= vy - g*dt
    y = y + vy*dt
    t += dt
    pomak_x.append(x)
    pomak_y.append(y)
    vrijeme.append(t)
    
plt.subplot(311)
plt.plot(pomak_x,pomak_y)
plt.subplot(312)
plt.plot(vrijeme,pomak_x)
plt.subplot(313)
plt.plot(vrijeme, pomak_y)
plt.show() 