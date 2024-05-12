import matplotlib.pyplot as plt
import numpy as np

class Cestica:
    def __init__(self, m, q, s, v, E, B, dt):
        self.m = m
        self.q = q
        self.s = np.array(s)
        self.v = np.array(v)
        self.E = np.array(E)
        self.B = np.array(B)
        self.dt = dt
    
    def gibanje(self, t):
        t0 = 0.0
        putanja = []
        vrijeme = np.arange(t0, t, self.dt)
        for i in vrijeme:
            a = (self.q/self.m) * (self.E + (np.cross(self.v, self.B)))
            self.v = self.v + a * self.dt
            self.s = self.s + self.v * self.dt
            putanja.append(self.s)
        return np.array(putanja)