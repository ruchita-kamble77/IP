#Pract4:- Illustration of Segmentation techniques.
#Create a python code to demonstrate image segmentation using varying techniques like Global Thresholding and Region Growing.

#Image Segmentation using Global Thresholding 

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray
import cv2

plt.figure(figsize=(6,6))
chico = imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\chico.jpg")
plt.imshow(chico);
th_values = np.linspace(0, 1, 11)
fig, axis = plt.subplots(2, 5, figsize=(15,8))

chico_gray = rgb2gray(chico)
for th, ax in zip(th_values, axis.flatten()):
    
    chico_binarized = chico_gray < th
    ax.imshow(chico_binarized)
    ax.set_title('$Threshold = %.2f$' % th)
    ax.axis("off")
plt.tight_layout()
plt.show()

# Ask user to select a threshold
user_input = input("Enter the threshold value you liked (e.g., 0.3): ")
try:
    final_th = float(user_input)
except ValueError:
    print("Invalid input. Using default threshold 0.5.")
    final_th = 0.5

# Apply final threshold and save/show
final_binarized = chico_gray < final_th

# Show the final image
plt.figure()
plt.imshow(final_binarized, cmap='gray')
plt.title(f'Final Thresholded Image @ {final_th:.2f}')
plt.axis('off')
plt.show()

# Save the final result
cv2.imwrite(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\chico_forged.png", (final_binarized * 255).astype('uint8'))
