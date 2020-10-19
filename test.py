import numpy as np
import matplotlib.pyplot as plt
import random
import math

theta = np.linspace(0, 2*np.pi, 100)
t=[]
ty=[]
surf=0
surface=[]
n=100000
r = np.sqrt(8)
bor=3
while(abs((r*r*math.pi)-surf)>0.001):

    n=n+100000
    surf=0
    for i in range(0, n):
        tempx = random.uniform(-bor,bor)
        tempy = random.uniform(-bor,bor)

        t.append(tempx)
        ty.append(tempy)

        if ((r >= t[len(t) - 1] or -r <= t[len(t) - 1]) and (
                (math.pow(t[len(t) - 1], 2) + math.pow(ty[len(ty) - 1], 2)) <= (r * r))):
            surf += 1
    surf=(surf / n) * bor*2 * bor*2
    surface.append(surf)
    print(abs((r*r*math.pi)-surf))
print(surface,r*r*math.pi)

"""
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
print((surf/n)*4*4)
fig, ax = plt.subplots(1)


ax.plot(x1, x2)
ax.set_aspect(1)
plt.scatter(t,ty)
plt.xlim(-2,2)
plt.ylim(-2,2)

plt.grid(linestyle='--')

plt.title('How to plot a circle with matplotlib ?', fontsize=8)

plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

plt.show()
"""
