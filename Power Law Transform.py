import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 
#this type of processing is suited for displaying image correctly for human eye based on monitor's display settings
# Read an image 
image = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\jungle.jpg") 
plt.imshow(image) 
plt.show()
# Trying 7 gamma values. 
for gamma in [0.1, 0.3, 0.4, 0.5, 1.2, 2.2, 3.2]: 

    # Apply gamma correction. 
    gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = 'uint8') 
    plt.imshow(gamma_corrected) 
    plt.show() 
