#Pract7:- Illustration of Image Forgery
#Create a Python code for demonstrating any image forgery method e.g. Copy-Move method.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\sunandmoon_forged.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Simulate forgery: Copy a region and paste it elsewhere
forged = image_rgb.copy()

# Define region to copy (e.g., a 50x50 square)
x1, y1, w, h = 328, 358, 40, 40
region = forged[y1:y1+h, x1:x1+w]

# Define where to paste the copied region
x2, y2 = 200, 358
forged[y2:y2+h, x2:x2+w] = region

x3, y3 = 456, 358
forged[y3:y3+h, x3:x3+w] = region

# Display original and forged images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(forged)
plt.title("Forged Image (Copy-Move)-Image from Outer Space Planet")
plt.axis("off")

plt.tight_layout()
plt.show()

cv2.imwrite(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\sunandmoon.png",forged)
