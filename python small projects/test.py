import numpy as np
import matplotlib.pyplot as plt
im = plt.imread('bird.jpg')
plt.imshow(np.flip(im, axis=1))
plt.show()
