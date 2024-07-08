import numpy as np
import matplotlib.pyplot as plt
from math import pi
holes = 100
ly = 4*10**(-7)
w = (2*pi*3*10**8)/ly
k = 2*pi/ly
a = 1
l = 0.4
h = 0.02
step = 0.05
xmin = -10
xmax = 10
x = xmin
T = 2*pi/w
t = T/50
f=0
xs = []
X = xmin
xn = np.array([])
ly1= 8*10**(-7)
w1=(2*pi*3*10**8)/ly1
k1=2*pi/ly1

ly2= 5*10**(-7)
w2=(2*pi*3*10**8)/ly2
k2=2*pi/ly2


ly3= 4.5*10**(-7)
w3=(2*pi*3*10**8)/ly3
k3=2*pi/ly3

T1 = 2*pi/w1
T2 = 2*pi/w2
T3 = 2*pi/w3
t1 = T1/50
t2 = T2/50
t3 = T3/50

while X<=xmax:
    xn = np.append(xn, X)
    X+=0.05
rl1 = []
rl2 = []

for i in range(holes):
    rl1.append((l**2+(xn-(h+0.005*i))**2)**0.5)
    rl2.append((l**2+(xn+(h+0.005*i))**2)**0.5)
rl = rl1 + rl2

rls = []
rls1 = []
rls2 = []
rls3 = []
for r in rl :
    rls.append(a*np.sin(k*r-w*t)/r)
    rls1.append(a*np.sin(k1*r-w1*t1)/r)
    rls2.append(a*np.sin(k2*r-w2*t2)/r)
    rls3.append(a*np.sin(k3*r-w3*t3)/r)
rls = np.array(rls)
rls1 = np.array(rls1)
rls2 = np.array(rls2)
rls3 = np.array(rls3)
lts = np.sum(rls, axis=0)
lts1 = np.sum(rls1, axis=0)
lts2 = np.sum(rls2, axis=0)
lts3 = np.sum(rls3, axis=0)
lts = lts**2
lts1 = lts1**2
lts2 = lts2**2
lts3 = lts3**2

xx = xmin
print('calc finished')
print(k1, k2, k3)
xx = xmin
for i, light_level in enumerate(lts) :
    xx += step
    plt.plot([xx, xx], [-1, -0.33], color=(lts1[i]/max(lts1), lts2[i]/max(lts2) , lts3[i]/max(lts3)))
plt.show()
