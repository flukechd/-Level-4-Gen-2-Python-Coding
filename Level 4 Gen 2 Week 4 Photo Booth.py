# PHOTOBOOTH
import cv2
import os
import numpy as np

print("\u2764\ufe0f")
# Path to the folder containing the images
folder_path = os.path.join('OutputImages')

# List all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Create a new blank image to hold the 4 images in a 4x4 layout
result = None

# Iterate over the first 4 image files
for i in range(4):
    # Open the image file
    image = cv2.imread(os.path.join(folder_path, image_files[i]))
    
    # Crop image
    if i == 0:
       # Create a blank mask image of the same size as the input image
        blank = np.zeros(image.shape[:2], dtype='uint8')
        # cv2.imshow('mask',mask)
        mask  = cv2.circle(blank.copy(), (310,230), 250, 255, -1)
        # cv2.imshow('c',circle)
        image = cv2.bitwise_and(image,image,mask=mask) 
        

    # Convert Color spaces
    elif i == 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    # Smoothing
    elif i == 2:
        image = cv2.blur(image, (7,7))
    
    # RGB Splitmerge
    elif i == 3:
        blank = np.zeros(image.shape[:2], dtype='uint8')
        b,g,r = cv2.split(image)
        image = cv2.merge([blank,g,blank])

    # Resize the image to fit a 200x200 square
    image = cv2.resize(image, (300, 300))
    
    # Add a yellow border around the image
    image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 255, 255))
    
    # Add the image to the result image
    if result is None:
        result = image
    else:
        result = cv2.hconcat([result, image])

# Add blue borders between the images
result = cv2.copyMakeBorder(result, 40, 40, 100, 40, cv2.BORDER_CONSTANT, value=(255, 0, 0))

# save the frame to an image file in the OutputImages folder
cv2.imwrite('OutputImages/namePhotoBooth.jpg', result)

# Show the result image
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
