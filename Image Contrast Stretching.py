#a.Contrast Stretching
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\low_contrast.jpg")

# Get min and max intensity values
min_val = np.min(img)
max_val = np.max(img)

# Apply contrast stretching formula
stretched = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)

# Display original and stretched image side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contrast Stretched")
plt.imshow(stretched, cmap='gray')
plt.axis('off')

plt.show()
