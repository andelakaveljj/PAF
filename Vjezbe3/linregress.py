import numpy as np
import matplotlib.pyplot as plt
M=[0.052,0.124,0.168,0.236,0.284,0.336]
fi=[0.1745,0.3491,0.5236,0.6981,0.8727,1.0472]
#y os je M, a x os fi
sumaM=sum(M)    #zbroj svih članova liste
sumafi=sum(fi)
arthM=sumaM/len(M)  #aritmetička sredina
arthfi=sumafi/len(fi)

a=arthM*arthfi/arthfi**2 #iz formule nađi a
y=0
m=[]
for el in fi:
    F = a* el
    m.append(F)

sigma = np.sqrt((1/len(M) * ((arthM**2/arthfi**2)-a**2)))

print(a)
plt.scatter(fi,M)
plt.plot(fi,m)
plt.title("D = {} +/- {}".format(round(a,9), round(sigma, 9)))
plt.show()