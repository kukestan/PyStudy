import numpy as np
import matplotlib.pyplot as plt
#线图和散点图
def draw_plot():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 100])

    plt.plot(xpoints, ypoints)
    plt.show()
x = [1, 2, 3]
y = [4, 5, 6]
plt.bar(y, x)
plt.show()
#x = np.arange(0, 6, 0.1)    #0, 0.1, 0.2, ... , 5.9, 6.0
#y = np.sin(x)
#plt.plot(x, y)
#plt.show()