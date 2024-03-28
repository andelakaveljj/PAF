import numpy as np
import matplotlib.pyplot as plt
import particle as part

t=0.001     #definiram neki dt
vrijeme=[]  
error=[]
while t<=0.1:   #za svaki dt koji je manji od 0.1
    p=part.Particle(10,60,0,0,t)    #stvaram česticu koja ima obilježja iz modula particle
    err=(np.abs(p.range()- p.analiticki_domet())/p.analiticki_domet())*100      #formula za pogrešku
    error.append(err)
    t=t+0.001
    vrijeme.append(t)
plt.plot(vrijeme,error)
plt.show()