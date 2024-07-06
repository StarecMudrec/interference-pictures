import numpy as np
import random
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
t = T/100
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
            rl1.append((l**2 + (xn-(0.005*i))**2)**0.5)
            rl2.append((l**2 + (xn+(0.005*i))**2)**0.5)
#rl1 = [(l**2 + (xn-h)**2)**0.5]
# print(holes)
rl = rl1 + rl2

'''for i in rl1:
    for j in range(len(i)):
           #el1[len(i)].append(np.sin(k*i[j]-w*t)/i[j])
           print(i[j])'''

rls = []
for o in rl :
    rls.append([])
for i in range(100) :
    t = random.randrange(0, 100)
    for j in range(len(rl)) :
        r = rl[j]
        rls[j].append(np.sin(k*r-w*t)/r)
#print(rls)
rts = []
for k in rls :
    rts.append(sum(k)/len(k))
rts = np.array(rts)
lts = np.sum(rts, axis=0)
lts = lts**2
lts2 = lts[:len(lts)//2]

print('calc finished')
xx = xmax
fig, ax = plt.subplots()
ax.set_aspect(1)
#lts2 = np.flip(lts2)
for light_level in lts2 :
    xx -= step
    circle = plt.Circle((0, 0), xx, color=(light_level/max(lts2), light_level/max(lts2), light_level/max(lts2)))
    #plt.plot([xx, xx], [-1, 1], color=(light_level/max(lts), light_level/max(lts), light_level/max(lts)))
    ax.add_artist(circle)

plt.figure(fig)
plt.xlim([xmin, xmax])
plt.ylim([xmin, xmax])
plt.show()


'''for i in r2:
       e2 = a*np.sin(k*i-w*t)/i'''
