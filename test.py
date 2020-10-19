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
r = np.sqrt(2.0)
while(abs(6.28318-surf)>0.001):

    n=n+100000
    surf=0
    for i in range(0, n):
        tempx = random.uniform(-2, 2)
        tempy = random.uniform(-2, 2)

        t.append(tempx)
        ty.append(tempy)

        if ((r >= t[len(t) - 1] or -r <= t[len(t) - 1]) and (
                (math.pow(t[len(t) - 1], 2) + math.pow(ty[len(ty) - 1], 2)) <= (r * r))):
            surf += 1
    surf=(surf / n) * 4 * 4
    surface.append(surf)
print(surface)
"""x1 = r*np.cos(theta)
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

plt.show()"""

