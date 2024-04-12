import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as hos

p1=hos.HarmonicOscillator(1,2,1,1)
a, v, x, t = p1.graf(10)
plt.subplot(1, 3, 1)
plt.plot(t, x)
plt.subplot(1, 3, 2)
plt.plot(t, v)
plt.subplot(1, 3, 3)
plt.plot(t, a)
plt.show()