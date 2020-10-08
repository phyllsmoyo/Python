import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.arange(10, 30, 0.23)
y = 3 * x ** 2 + 5 * x + 3

plt.plot(x, y)
plt.show()