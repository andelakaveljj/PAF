import numpy as np
import matplotlib.pyplot as plt
import math

class HarmonicOscillator:
    def __init__(self,m,k,x0,v0,dt = 0.01):
        self.m=m
        self.k=k
        self.x0=x0
        self.v0=v0
        self.dt = dt
        self.list_a=[]
        self.list_x=[]
        self.list_v=[]
        self.vrijeme=[]
    
    def graf(self,t):
        t0=0
        while t0<=t:
            a0=-(self.k/self.m)*self.x0
            self.list_a.append(a0)
            self.v0=self.v0+a0*self.dt    #početnu brzinu računam kao a*t, ali kako se povećava dt odnosno vrijeme onda raste i brzina
            self.list_v.append(self.v0)
            self.x0=self.x0+self.v0*self.dt
            self.list_x.append(self.x0)
            self.vrijeme.append(t0)
            t0=t0+self.dt
        return self.list_a,self.list_v,self.list_x,self.vrijeme
    
    def analiticki_graf(self, t):
        vremena=np.arange(0, t, self.dt)
        omega=np.sqrt(self.k/self.m)
        amplituda=np.sqrt(self.x0**2+(self.v0/omega)**2)
        if self.x0==0:
            if self.v0>0:
                fi=0.5*np.pi
            else:
                fi=-0.5*np.pi
        else:
            fi=np.arctan(-self.v0/(omega*self.x0))
        x=amplituda*np.cos(omega*vremena+fi)
        return x,vremena