import matplotlib.pyplot as plt
from math import sin, cos

def jednoliko_gibanje(F,m,t):
    a = F/m
    dt = 0.1
    N = t*10
    v=0
    x=0
    t=0
    akceleracija=[]
    brzina=[]
    pomak=[]
    vrijeme=[]

    for i in range(N):
        v= v + a*dt
        x = x + v*dt
        t += dt
        brzina.append(v)
        pomak.append(x)
        vrijeme.append(t)
        akceleracija.append(a)

    plt.subplot(311)
    plt.plot(vrijeme,pomak)
    plt.title('x-t graf')
    plt.subplot(312)
    plt.plot(vrijeme,brzina, 'r')
    plt.title('v-t graf')
    plt.subplot(313)
    plt.plot(vrijeme,akceleracija, 'g')
    plt.title('a-t graf')
    plt.show()


def kosi_hitac(v0,theta,t):
    vx=v0*cos(theta)
    vy=v0*sin(theta)
    y=0
    x=0
    dt=0.5
    g=9.81
    N=t*2
    pomak_x=[]
    pomak_y=[]
    vrijeme=[]
    for i in range(N):
        x=x + vx*dt
        vy=vy - g*t
        y=y + vy*dt
        t += dt
        pomak_x.append(x)
        pomak_y.append(y)
        vrijeme.append(t)
        
    plt.subplot(311)
    plt.plot(pomak_x,pomak_y)
    plt.title('x-y graf')
    plt.subplot(312)
    plt.plot(vrijeme,pomak_x)
    plt.title('x-t graf')
    plt.subplot(313)
    plt.plot(vrijeme, pomak_y)
    plt.title('y-t graf')
    plt.show() 