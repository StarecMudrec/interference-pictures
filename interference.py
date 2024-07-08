import numpy as np
import matplotlib.pyplot as plt
from math import pi 
holes = 100
ly= 4*10**(-7)
w=(2*pi*3*10**8)/ly
k=2*pi/ly
a=1
l=0.4
h=0.02
step = 0.02
xmin = -5
xmax = 5
x=xmin
c=3*10**8
T = 2*pi/w
t = T/50
f=0
xs = []
X = xmin
el1=[]
el2 = []
xn = np.array([])


while X<=xmax:
    xn = np.append(xn, X)
    X+=step
rl1 = []
rl2 = []

for i in range(holes):
            rl1.append((l**2 + (xn-(h+0.005*i))**2)**0.5)
            rl2.append((l**2+(xn+(h+0.005*i))**2)**0.5)
#rl1 = [(l**2 + (xn-h)**2)**0.5]
# print(holes)
rl = rl1 + rl2

'''for i in rl1:
    for j in range(len(i)):
           #el1[len(i)].append(np.sin(k*i[j]-w*t)/i[j])
           print(i[j])'''

rls = []
for r in rl :
    rls.append(np.sin(k*r-w*t)/r)
rls = np.array(rls)
lts = np.sum(rls, axis=0)
lts = lts**2

print('calc finished')
xx = xmin
for light_level in lts :
    xx += step
    plt.plot([xx, xx], [-1, 1], color=(light_level/max(lts), light_level/max(lts), light_level/max(lts)))
plt.show()


'''for i in r2:
       e2 = a*np.sin(k*i-w*t)/i'''