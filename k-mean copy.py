import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("training_data/latih_01.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.imread("training_data/latih_01.jpg", cv2.IMREAD_GRAYSCALE)
# gi = cv2.imwrite('gray_img_1.png', gray_image)

# co = cv2.imread("training_data/latih_01.jpg")

# cv2.imshow("Gray Image", co)

# cv2.waitKey(0)

# image_rgb = cv2.cvtColor(co, cv2.COLOR_BGR2RGB) 

# Apply Canny edge detection 
# edges = cv2.Canny(image= image_rgb, threshold1=100, threshold2=700) 
  
# Create subplots 
fig, axs = plt.subplots(1, 2, figsize=(7,4)) 

axs[0].imshow(gray_image)
axs[0].set_title("Gray 1")
axs[1].imshow(gray_image2)
axs[1].set_title("Gray 2")
# Plot the original image 
# axs[0].imshow(image_rgb) 
# axs[0].set_title('Original Image') 
  
# # Plot the blurred image 
# axs[1].imshow(edges) 
# axs[1].set_title('Image edges') 
  
# Remove ticks from the subplots 
for ax in axs: 
    ax.set_xticks([]) 
    ax.set_yticks([]) 
  
# Display the subplots 
plt.tight_layout() 
plt.show()
