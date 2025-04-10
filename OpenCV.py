import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image.jpg.png')  # Replace with your image filename
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(img_rgb, (5, 5), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(img_rgb, 5)

# Show the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gaussian_blur)
plt.title('Gaussian Filter')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(median_blur)
plt.title('Median Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
