import math
import matplotlib.pyplot as plt
import numpy as np
class Particle:
    def __init__(self, v, kut, x0, y0, dt=0.1):
        self.g=9.81
    
    def reset(self):
        self.vx0=0
        self.vy0=0
        self.kut=0
        self.x0=0
        self.y0=0
    
    def __move(self):
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1]-self.dt*0)
        self.vy.append(self.vy[-1]-self.dt*self.g)
        self.t.append(self.t[-1]+self.dt)

    def range(self):
        while(self.y[-1]>=0):
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):
        self.vx0=0
        self.vy0=0
        self.kut=0
        self.x0=0
        self.y0=0
        self.vx.append(self.vx[-1]-self.dt*0)
        self.vy.append(self.vy[-1]-self.dt*self.g)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.t.append(self.t[-1]+self.dt)
        while(self.y[-1]>=0):
            self.__move()
        plt.plot(self.x, self.y)
        plt.show()