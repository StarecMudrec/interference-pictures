import numpy as np
import matplotlib.pyplot as plt
from math import pi 
holes = 2
ly= 4*10**(-7)
w=(2*pi*3*10**8)/ly
k=2*pi/ly
a=1
l=0.4
h=0.02
xmin = -10
xmax = 10
x=xmin
c=3*10**8
T = 2*pi/w
t = T/50
step = 0.05
from posixpath import join
import math
import numpy as np
def wl2rgb_pregamma(wl):
    if wl >= 380 and wl < 440:
        s = 0.3 + (0.7 * (wl - 380.0)) / (420.0 - 380.0) if wl < 420 else 1.0
        return [-1 * (wl - 440) / (440 - 380), 0, s]
    elif wl >= 440 and wl < 490:
        return [0, (wl - 440) / (490 - 440), 1]
    elif wl >= 490 and wl < 510:
        return [0, 1, -1 * (wl - 510) / (510 - 490)]
    elif wl >= 510 and wl < 580:
        return [(wl - 510) / (580 - 510), 1.0, 0.0]
    elif wl >= 580 and wl < 645:
        return [1, -1 * (wl - 645) / (645 - 580), 0]
    elif wl > 700:
        return [0.3 + (0.7 * (780 - wl)) / (780 - 700), 0, 0]
    else:
        return [0, 0, 0]

def wl2rgb(wl):
    gamma = 0.8
    r, g, b = wl2rgb_pregamma(wl)
    return [math.pow(r, gamma), math.pow(g, gamma), math.pow(b, gamma)]
f=0
xs = []
X = xmin
el1=[]
goals = 1000
el2 = []
xn1 = np.array([])
xn2 = np.array([])
xn3 = np.array([])
step = 0.05

ly1= 6.5*10**(-7)
w1=(2*pi*3*10**8)/ly1
k1=2*pi/ly1
T1 = 2*pi/w1
t1 = T1/100

ly2= 5.1*10**(-7)
w2=(2*pi*3*10**8)/ly2
k2=2*pi/ly2
T2 = 2*pi/w2
t2 = T2/100

ly3=4.4*10**(-7)
w3=(2*pi*3*10**8)/ly3
k3=2*pi/ly2
T3 = 2*pi/w3
t3 = T3/100

while X<=xmax:
    xn1 = np.append(xn1, X)
    xn2 = np.append(xn2, X)
    xn3 = np.append(xn3, X)
    X+=step
rl1 = []
rl2 = []
rl3 = []
rl4 = []
rl5 =[]
rl6= []

for j in range(goals):
  for i in range(holes):
    rl1.append((l**2+(xn1-(h*(1+j)+0.005*i))**2)**0.5)
    rl2.append((l**2+(xn1+(h*(1+j)+0.005*i))**2)**0.5)
    rl3.append((l**2+(xn2-(h*(1+j)+0.005*i))**2)**0.5)
    rl4.append((l**2+(xn2+(h*(1+j)+0.005*i))**2)**0.5)
    rl5.append((l**2+(xn3-(h*(1+j)+0.005*i))**2)**0.5)
    rl6.append((l**2+(xn3+(h*(1+j)+0.005*i))**2)**0.5)

rl = rl1 + rl2 
rll = rl3 + rl4
rll3 = rl5+rl6
rls1 = []
rls2 = []
rls3 = []

for r in rl :
    rls1.append(a*np.sin(k1*r-w1*t1)/r)
for m in rll:
    rls2.append(a*np.sin(k2*m-w2*t2)/m)
for q in rll3:
    rls3.append(a*np.sin(k3*m-w3*t3)/q)   
rls1 = np.array(rls1) #E1
rls2 = np.array(rls2)#E2
rls3 = np.array(rls3)#E3

lts1 = np.sum(rls1, axis=0)#sume1
lts2 = np.sum(rls2, axis=0)#sume2
lts3 = np.sum(rls3, axis = 0)#sume3

jo1= (lts1**2)/max(lts1**2)#I of red
jo2 = (lts2**2)/max(lts2**2)#I of green
jo3 = (lts3**2)/max(lts3**2)#I of blue
ygrt1= jo1*650 #red power
ygrt2 = jo2*510 #green power
ygrt3 = jo3*440 #blue power
oras = (lts1+lts2+lts3)**2/max((lts1+lts2+lts3)**2) #I
oras = np.array(oras)
hg= [] #color(r,g,b)
ss=[] #power + color

for i in range(len(ygrt1)):
  hg.append([(wl2rgb(ygrt1[i])[0]+wl2rgb(ygrt2[i])[0]+wl2rgb(ygrt3[i])[0])/3,(wl2rgb(ygrt1[i])[1]+wl2rgb(ygrt2[i])[1]+wl2rgb(ygrt2[i])[1])/3,(wl2rgb(ygrt1[i])[2]+wl2rgb(ygrt2[i])[2]+wl2rgb(ygrt2[i])[2])/3])
print(hg)
for i in range(len(ygrt1)):
  ss.append((oras[i]*np.array(hg[i])))
print('calc finished')
hg = np.array(hg)
xx = xmin
for light_level in ss :
    xx += step
    plt.plot([xx, xx], [-1, 1], color=(light_level))
plt.show()
