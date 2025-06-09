#Create PYTHON CODE to transform an image in special domain into
#its frequency domain using DFT


import numpy as np
import matplotlib.pyplot as plt
image_filename = r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\mobile.webp"

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    return np.fft.fftshift(ft)
# Read and process image
image = plt.imread(image_filename)
image = image[:, :, :3].mean(axis=2)  # Convert to grayscale
plt.set_cmap("gray")
ft = calculate_2dft(image)
plt.subplot(121)
plt.imshow(image)
plt.axis("off")
plt.subplot(122)
plt.imshow(np.log(abs(ft)))
plt.axis("off")
plt.show()
