import matplotlib.pyplot as plt
import numpy as np
import harmonic_oscillator as hos

p1 = hos.HarmonicOscillator(1, 5, 2, 2, 0.1)
p2 = hos.HarmonicOscillator(1, 5, 2, 2, 0.05)
p3 = hos.HarmonicOscillator(1, 5, 2, 2, 0.01)

a1, v1, x1, t1 = p1.graf(7)
a2, v2, x2, t2 = p2.graf(7)
a3, v3, x3, t3 = p3.graf(7)
x,t=p3.analiticki_graf(7) 
plt.scatter(t3, x3, s = 2)
plt.scatter(t2, x2, s = 2)
plt.scatter(t1, x1, s = 2)
plt.plot(t,x)
plt.show()