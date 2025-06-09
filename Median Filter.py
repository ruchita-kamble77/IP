from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

im = Image.open(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practs\averaging.jpg")
im1 = im.filter(ImageFilter.MedianFilter(size = 7))

plt.subplot(121),plt.imshow(im),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im1),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
