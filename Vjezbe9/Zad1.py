import matplotlib.pyplot as plt
import numpy as np
import gravitacija as grav

m1=1.989*10**30  #masa sunca
m2=5.9742*10**24 #masa zemlje
t=365.242

A1=grav.Gravitacija(m1,m2,(0,0),(1.486*10**11,0),(0,0),(0,29783),1)
s,z=A1.Euler(t)

plt.plot(z[:,0],z[:,1])
plt.plot(s[:,0],s[:,1], "o")
plt.show()