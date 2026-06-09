import numpy as np

import matplotlib.pyplot as plt

a = np.array([1,2])
b = np.array([3, 0])

c = a + b

print("a + b =", c)

plt.quiver(0, 0, a[0], a[1], angles="xy", scale_units="xy", scale=1, color="blue", label="a")
plt.quiver(0, 0, b[0], b[1], angles="xy", scale_units="xy", scale=1, color="green", label="b")
plt.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='red',   label='a+b')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
