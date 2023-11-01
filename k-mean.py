import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("training_data/latih_01.jpg")

# print(img.shape)

red_channel = img[:,:,2]
green_channel = img[:,:,1]
blue_channel = img[:,:,0]
print(red_channel)

# Write red channel to greyscale image
cv2.imwrite('cv2-red-channel.png', red_channel)
cv2.imwrite('cv2-green-channel.png', green_channel)
cv2.imwrite('cv2-blue-channel.png', blue_channel)

def display_to(co) : 
    fig, axs = plt.subplots(1, 2, figsize=(7,4))
    image_rgb = cv2.cvtColor(co, cv2.COLOR_BGR2RGB)

    axs[0].imshow(image_rgb)
    axs[0].set_title("Original Image")


    red_channel = img[:, :, 2]
    green_channel = img[:,:,1]
    blue_channel = img[:,:,0]

    axs[1].imshow(red_channel)
    axs[1].set_title("Red Channel Image")
    
    axs[1].imshow(blue_channel)
    axs[1].set_title("blue Channel Image")

    axs[1].imshow(green_channel)
    axs[1].set_title("Green Channel Image")
    # Remove ticks from the subplots
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Display the subplots
    plt.tight_layout()
    plt.show()

display_to(img)
