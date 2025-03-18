

import cv2 as cv
import numpy as np

# Function to display an image
def display_image(title, img):
    cv.imshow(title, img)
    cv.waitKey(1)

# Apply dreamy glow effect
def dreamy_glow_effect(img, blur_strength, blend_strength):
    # Ensure blur_strength is an odd number for GaussianBlur kernel
    if blur_strength % 2 == 0:
        blur_strength += 1  
    # Apply Gaussian Blur
    blurred_image = cv.GaussianBlur(img, (blur_strength, blur_strength), 0) 
    # Blend the original and blurred image
    glowing_image = cv.addWeighted(img, 1 - blend_strength, blurred_image, blend_strength, 0)
    
    return glowing_image

# Apply grayscale conversion
def convert_grayscale(img, graylevel):
    first_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    final_gray = cv.cvtColor(first_gray, cv.COLOR_GRAY2BGR)
    percent = graylevel/100.0
    return cv.addWeighted(img, 1 - percent, final_gray, percent, 0)

# Function to adjust RGB values
def adjust_rgb(img, red_value, green_value, blue_value):
    # Create a blank image with the same size as the original
    adjusted_image = img.copy()
    
    #covert percentage
    bluefactor = blue_value / 100.0
    greenfactor = green_value / 100.0
    redfactor = red_value / 100.0

    # Adjust each channel (R, G, B) based on slider values
    adjusted_image[:, :, 0] = np.clip(adjusted_image[:, :, 0] * bluefactor, 0, 255) 
    adjusted_image[:, :, 1] = np.clip(adjusted_image[:, :, 1] * greenfactor, 0, 255)  
    adjusted_image[:, :, 2] = np.clip(adjusted_image[:, :, 2] * redfactor, 0, 255)  
    
    return adjusted_image

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    scale = 1.0  # Scaling factor
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv.warpAffine(img, M, (w, h))
    return rotated_image

def zoom_image(img, scale):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    angle = 0  # Scaling factor
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv.warpAffine(img, M, (w, h))
    return rotated_image

# Callback function for the trackbars
def on_trackbar(val):
    # Empty function to handle trackbar events; no recursive calls inside here
    pass

# Load the image
image = cv.imread("image1.jpg")
if image is None:
    print("Failed to load image.")

# Create a window
cv.namedWindow('Dreamy Glow Effect')

cv.createTrackbar('Blur', 'Dreamy Glow Effect', 0, 100, on_trackbar)  # Defaul value 15, max 50
cv.createTrackbar('Blend', 'Dreamy Glow Effect', 0, 100, on_trackbar) # Default value 70 (0.7)
cv.createTrackbar('Gray', 'Dreamy Glow Effect', 0, 100, on_trackbar)
cv.createTrackbar('Red', 'Dreamy Glow Effect', 100, 200, on_trackbar)  
cv.createTrackbar('Green', 'Dreamy Glow Effect', 100, 200, on_trackbar)
cv.createTrackbar('Blue', 'Dreamy Glow Effect', 100, 200, on_trackbar)
cv.createTrackbar('Zoom', 'Dreamy Glow Effect', 1, 200, on_trackbar)  
cv.createTrackbar('Rotate', 'Dreamy Glow Effect', 0, 360, on_trackbar)  



while True:
    # Get trackbar positions
    blur_strength = cv.getTrackbarPos('Blur', 'Dreamy Glow Effect')
    blend_strength = cv.getTrackbarPos('Blend', 'Dreamy Glow Effect') / 100.0
    gray_level = cv.getTrackbarPos('Gray', 'Dreamy Glow Effect')
    red_value = cv.getTrackbarPos('Red', 'Dreamy Glow Effect')
    green_value = cv.getTrackbarPos('Green', 'Dreamy Glow Effect')
    blue_value = cv.getTrackbarPos('Blue', 'Dreamy Glow Effect')
    angle = cv.getTrackbarPos('Rotate', 'Dreamy Glow Effect')
    zoom_level = cv.getTrackbarPos('Zoom', 'Dreamy Glow Effect')

    # Apply the dreamy glow effect
    glowing_image = dreamy_glow_effect(image, blur_strength, blend_strength)
        
    # Adjust grayscale
    glowing_image = convert_grayscale(glowing_image, gray_level)
        
    # Adjust RGB values
    glowing_image = adjust_rgb(glowing_image, red_value, green_value, blue_value)

    #rotate the image 
    glowing_image = rotate_image(glowing_image, angle)

    #zoom the image 
    glowing_image = zoom_image(glowing_image, zoom_level)

    # Display the updated image
    display_image('Dreamy Glow Effect', glowing_image)

    # Wait for the user to press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

# Close all windows
cv.destroyAllWindows()


