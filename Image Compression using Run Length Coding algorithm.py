#Pract5:- Image Compression Technique
#Create python code for demonstrating Image Compression using Run Length Coding algorithm.

import numpy as np
import cv2  # or use imageio if you prefer

def rle_encode(arr):
   # Encode 1D numpy array using Run-Length Encoding.
   # Returns list of (value, count) pairs.
    
    if len(arr) == 0:
        return []

    encoded = []
    prev_value = arr[0]
    count = 1

    for val in arr[1:]:
        if val == prev_value:
            count += 1
        else:
            encoded.append((prev_value, count))
            prev_value = val
            count = 1
    encoded.append((prev_value, count))
    return encoded


def rle_decode(encoded):
        # Decode RLE-encoded data back to 1D numpy array.
    decoded = []
    for value, count in encoded:
        decoded.extend([value] * count)
    return np.array(decoded, dtype=np.uint8)

# Load grayscale image
image = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\ico_warning.png", cv2.IMREAD_GRAYSCALE)
# Flatten to 1D
flat_image = image.flatten()
print("Original Length:",len(flat_image))

# Encode
encoded = rle_encode(flat_image)
print("Encoded length:", len(encoded))

# Decode
decoded_flat = rle_decode(encoded)

# Reshape back to original shape
decoded_image = decoded_flat.reshape(image.shape)

# Save reconstructed image to verify
cv2.imwrite(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practicals\ico_warning_decode.png", decoded_image)
