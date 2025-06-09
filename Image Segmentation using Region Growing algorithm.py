#Image Segmentation using Region Growing algorithm

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation

# Original image (imaginary region to be filled)
A = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
# Complement of original image
Ac = 1 - A

# Structuring element
B = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

# Seed point to start filling
x = np.zeros_like(A)
x[2, 2] = 1

# Visualization setup
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
plt.gray()

# Show original image
axs[0].imshow(A)
axs[0].set_title("Original A")

# Region filling loop
k = 0
flag_region_found = False

while not flag_region_found:
    k += 1
    axs[1].imshow(x)
    axs[1].set_title(f"Filling iteration {k}")
    plt.pause(0.6)

    xnew = np.logical_and(binary_dilation(x, B), Ac)
    diff = xnew.astype(int) - x.astype(int)

    if np.sum(diff) == 0:
        flag_region_found = True
    else:
        x = xnew

# Combine filled region with original
y = np.logical_or(x, A)

axs[2].imshow(y)
axs[2].set_title("Final Filled Region")
plt.tight_layout()
plt.show()
