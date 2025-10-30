import math
import matplotlib.pyplot as plt

root = []
g = lambda x: math.exp(-x)
x0 = 0

for i in range(20):
    x1 = g(x0)
    dif = abs(x1-x0)
    root.append(dif)
    x0 = x1

plt.plot(root)
plt.show()
