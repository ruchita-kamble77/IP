#Pract6:- Various Image Retrieval Techniques
#Create Python code for demonstrating techniques for Feature Detection in an Image.

#Edge Based Feature detection using Canny algorithm.
import cv2
import matplotlib.pyplot as plt

# Load image and convert to grayscale
img = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\4shapes.png", cv2.IMREAD_GRAYSCALE)

# Extract edges using Canny
edges = cv2.Canny(img, threshold1=100, threshold2=200)

# Show result
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Features')
plt.axis('off')
plt.show()
