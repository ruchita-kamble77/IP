# import Pillow modules

import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter
import math
# Compute log
def logTransform(c, f):
    g = c * math.log(float(1 + f),10);
    return g;

 # Apply logarithmic transformation for an image  
def logTransformImage(image, outputMax = 255, inputMax=255):
    c = outputMax/math.log(inputMax+1,10);
    print(c)
 
    # Read pixels and apply logarithmic transformation
    for i in range(0, img.size[0]-1):
        for j in range(0, img.size[1]-1):
            # Get pixel value at (x,y) position of the image
            f = img.getpixel((i,j));

             # Do log transformation of the pixel
            redPixel    = round(logTransform(c, f[0]));
            greenPixel  = round(logTransform(c, f[1]));
            bluePixel   = round(logTransform(c, f[2]));

            # Modify the image with the transformed pixel values
            img.putpixel((i,j),(redPixel, greenPixel, bluePixel));

    return image;

# Display the original image
imageFileName = r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\jungle.jpg";
img = Image.open(imageFileName);
#img.show()
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

# Display the image after applying the logarithmic transformation
logTransformedImage = logTransformImage(img);
#logTransformedImage.show();
plt.subplot(122),plt.imshow(logTransformedImage),plt.title('logTransformedImage')
plt.xticks([]), plt.yticks([])
plt.show()

