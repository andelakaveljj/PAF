import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,m,x0,y0,v0,ro,A,CD,k, dt=0.01):
        self.m=m
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.ro=ro
        self.A=A
        self.CD=CD
        self.k=k
        self.dt = dt
        self.ax=[]
        self.ay=[]
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]

    def Euler(self):
        t0=0
        g=9.81
        v0x=self.v0 * np.cos((self.k/180)*np.pi)
        v0y=self.v0*np.sin((self.k/180)/np.pi)
        while self.y0>=0:
            ax0 = -np.sign(v0x) * ((self.ro * self.CD * self.A) / 2*self.m) * (v0x**2)
            self.ax.append(ax0)
            v0x =v0x+ ax0 * self.dt
            self.vx.append(v0x)
            self.x0 =self.x0+ v0x * self.dt
            self.x.append(self.x0)
            ay0 = - g -np.sign(v0y) * ((self.ro * self.CD * self.A) / 2*self.m) * (v0y**2)
            self.ay.append(ay0)
            v0y =v0y+ ay0 * self.dt
            self.vy.append(v0y)
            self.y0 =self.y0+ v0y * self.dt
            self.y.append(self.y0)
            t0=t0+self. dt
        return self.x,self.y
    
    def Runge_Kutta(self):
        g = -9.81
        t0 = 0.0
        s = (self.ro * self.CD * self.A) / (2 * self.m)
        vx0 = self.v0 * np.cos((self.k / 180) * np.pi)  
        vy0 = self.v0 * np.sin((self.k / 180) * np.pi)
        while self.y0 >= 0:

            k1vx = (-np.sign(vx0) * s * (vx0)**2) * self.dt
            k1x = vx0 * self.dt
            k2vx =  (-np.sign(vx0 + (k1vx/2)) * s * (vx0 + (k1vx/2))**2) * self.dt
            k2x = (vx0 + (k1vx/2)) * self.dt
            k3vx =  (-np.sign(vx0 + (k2vx/2)) * s * (vx0 + (k2vx/2))**2) * self.dt
            k3x = (vx0 + (k2vx/2)) * self.dt
            k4vx =  (-np.sign(vx0 + (k3vx/2)) * s * (vx0 + (k3vx/2))**2) * self.dt
            k4x = (vx0 + (k3vx/2)) * self.dt
            
            vx0 = vx0 + ((1/6) * (k1vx + 2*k2vx + 2*k3vx + k4vx))
            self.x0 = self.x0 + ((1/6) * (k1x + 2*k2x + 2*k3x + k4x))

            k1vy = (g-np.sign(vy0) * s * (vy0)**2) * self.dt
            k1y = vy0 * self.dt
            k2vy =  (g-np.sign(vy0 + (k1vy/2)) * s * (vy0 + (k1vy/2))**2) * self.dt
            k2y = (vy0 + (k1vy/2)) * self.dt
            k3vy =  (g-np.sign(vy0 + (k2vy/2)) * s * (vy0 + (k2vy/2))**2) * self.dt
            k3y = (vy0 + (k2vy/2)) * self.dt
            k4vy =  (g-np.sign(vy0 + (k3vy/2)) * s * (vy0 + (k3vy/2))**2) * self.dt
            k4y = (vy0 + (k3vy/2)) * self.dt
            
            vy0 =vy0+((1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy))
            self.y0 = self.y0+((1/6) * (k1y + 2*k2y + 2*k3y + k4y))

            t0 =t0+ self.dt
            self.x.append(self.x0)
            self.y.append(self.y0)

        return self.x,self.y