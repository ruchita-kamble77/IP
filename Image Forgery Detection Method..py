#Pract8:- Illustration of Image Forgery Detection Method.
#Create a python code to detect if any forgery is made in an image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def embed_watermark(image, watermark_text):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Apply DCT
    dct = cv2.dct(gray)

    # Embed watermark text as ASCII into DCT coefficients
    watermark = [ord(c) for c in watermark_text]   #ord gives ASCII code for every character in watermark_text
    for i, val in enumerate(watermark):
        dct[0, i] += val % 10  # Embed only the last digit of the ASCII code into only in low-frequency band (top row)

    # Apply inverse DCT
    watermarked_img = cv2.idct(dct)
    watermarked_img = np.uint8(np.clip(watermarked_img, 0, 255))

    return watermarked_img


# Load original image
image = cv2.imread(r"D:\Ruchita\Information_Technology\MSC-IT(CC)\SEM2\Practs\sunandmoon_forged.png")
watermarked = embed_watermark(image, "AUTHENTIC")

""" Simulate forgery by tampering with image"""

tampered = watermarked.copy()
tampered[358:398, 328:368] = 255  # White patch (fake object)

# Show images
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(watermarked, cmap='gray')
plt.title("Watermarked Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(tampered, cmap='gray')
plt.title("Tampered Image")
plt.axis("off")
plt.tight_layout()
plt.show()

"""
#Checking Image for Forgery
"""

def extract_watermark(image, length):
    # Convert to grayscale and DCT
    gray = np.float32(image)
    dct = cv2.dct(gray)

    # Extract the embedded values
    extracted = ""
    for i in range(length):
        char_val = int(dct[0, i]) % 10
        extracted += str(char_val)

    return extracted

# Try to extract watermark from both images
wm_extracted_clean = extract_watermark(watermarked, len("AUTHENTIC"))
wm_extracted_tampered = extract_watermark(tampered, len("AUTHENTIC"))

print("Extracted from watermarked image:", wm_extracted_clean)
print("Extracted from tampered image:", wm_extracted_tampered)

if wm_extracted_clean != wm_extracted_tampered:
    print("\n⚠️ Forgery Detected: Watermark integrity compromised.")
else:
    print("\n✅ Image appears to be authentic.")
