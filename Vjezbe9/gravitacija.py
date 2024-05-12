import numpy as np
import matplotlib.pyplot as plt

class Gravitacija:
    def __init__(self,m1,m2,r1=(0,0),r2=(0,0),v1=(0,0),v2=(0,0),dt=1):
        self.r1=np.array(r1)
        self.r2=np.array(r2)
        self.m1=m1
        self.m2=m2
        self.v1=np.array(v1)
        self.v2=np.array(v2)
        self.dt=dt*24*60*60
        self.G=-6.67*(10**(-11))
        self.g = -9.81
        self.rad1=[]
        self.rad2=[]

    def Euler(self,t):
        t=t*24*3600
        t0=0
        while t0<=t:
            a1=(self.G*self.m2/(np.linalg.norm(self.r1 - self.r2)**3))*(self.r1 - self.r2)
            self.v1=self.v1+a1*self.dt
            self.r1=self.r1+self.v1*self.dt
            self.rad1.append(self.r1)

            a2=(self.G*self.m1/(np.linalg.norm(self.r2 - self.r1)**3))*(self.r2 - self.r1)
            self.v2=self.v2+a2*self.dt
            self.r2=self.r2+self.v2*self.dt
            self.rad2.append(self.r2)
            
            t0=t0+self.dt
        return np.array(self.rad1),np.array(self.rad2)

