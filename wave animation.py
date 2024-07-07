import  numpy as np
from math import pi
import matplotlib.pyplot as plt

t = 0
ly= 5*10**(-7)
w=(2*pi*3*10**8)/ly
k=2*pi/ly

xs = []
X = 0
while X <= 0.000001 :
    xs.append(X)
    X += 0.00000001
xs = np.array(xs)
for i in range(1000) :
    t += 1e-17
    ys = []
    Y = 0
    # for x in xs :
    #     Y = np.cos(k*x - w*t)
    #     ys.append(Y)
    print(w*t)
    ys = np.cos(k*xs - w*t)/xs
    #print(k, w, k*X, w*t, np.min(ys))
    plt.plot(xs, ys)
    plt.xlim([0,1e-6])
    plt.ylim([-1,1])
    plt.pause(0.001)
    plt.clf()
plt.show()