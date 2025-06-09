#Detecting Keypoint Descriptors (SIFT algorithm)
#Scale-Invariant Feature Transform (SIFT)
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:/Ruchita/Information_Technology/MSC-IT(CC)/SEM2/Practicals/4shapes.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SIFT object and detect keypoints
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)
print(descriptors)
# Draw keypoints
img_kp = cv2.drawKeypoints(img, keypoints, None)

plt.imshow(cv2.cvtColor(img_kp, cv2.COLOR_BGR2RGB))
plt.title('SIFT Keypoints')
plt.axis('off')
plt.show()
