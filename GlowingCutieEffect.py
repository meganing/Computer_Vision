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

# Function to adjust RGB values
def adjust_rgb(img, red_value, green_value, blue_value):
    # Create a blank image with the same size as the original
    adjusted_image = img.copy()
    
    # Convert percentage
    bluefactor = blue_value / 100.0
    greenfactor = green_value / 100.0
    redfactor = red_value / 100.0

    # Adjust each channel (R, G, B) based on slider values
    adjusted_image[:, :, 0] = np.clip(adjusted_image[:, :, 0] * bluefactor, 0, 255) 
    adjusted_image[:, :, 1] = np.clip(adjusted_image[:, :, 1] * greenfactor, 0, 255)  
    adjusted_image[:, :, 2] = np.clip(adjusted_image[:, :, 2] * redfactor, 0, 255)  
    
    return adjusted_image

# Apply contour effect with Bilateral Blur, Gaussian Blur, and Canny Edge Detection
def apply_contours(img, contour_color, contour_thickness):
    
    # Convert to grayscale for Canny edge detection
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection with fixed thresholds
    edges = cv.Canny(gray, 50, 150) 
    
    # Find contours
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on a copy of the original image
    contour_img = img.copy()
    cv.drawContours(contour_img, contours, -1, contour_color, contour_thickness)
    
    return contour_img

# Callback function for the trackbars
def on_trackbar(val):
    pass

# Load the image
image = cv.imread("image1.jpg")
cv.imshow("Original",image)
if image is None:
    print("Failed to load image.")

# Convert the image to grayscale to get the luminance
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply Bilateral Filter
bilateral_blur = cv.bilateralFilter(gray_image, 9, 75, 75)

# Further smooth the image with Gaussian Blur
blurred_image = cv.GaussianBlur(bilateral_blur, (3, 3), 0)

# Define the luminance threshold and apply simple thresholding
threshold_value = 120  # Set this value based on your needs (0 to 255)
_, mask = cv.threshold(blurred_image, threshold_value, 255, cv.THRESH_BINARY)

# Apply the mask to the original image to get the foreground in color
foreground = cv.bitwise_and(image, image, mask=mask)

# # Increase brightness of the foreground
# brightness_value = 50  # Adjust this value to control brightness
# bright_foreground = cv.add(foreground, (brightness_value, brightness_value, brightness_value, 0))

# Invert the mask to get the background
background_mask = cv.bitwise_not(mask)

# Apply the inverted mask to the original image to keep only the background
background = cv.bitwise_and(image, image, mask=background_mask)

# Combine the foreground with the original background
final_result = cv.add(foreground, background)

# Create a window
cv.namedWindow('Dreamy Glow Effect')

# Trackbars for dreamy glow effect
cv.createTrackbar('Blur', 'Dreamy Glow Effect', 1, 100, on_trackbar)
cv.createTrackbar('Blend', 'Dreamy Glow Effect', 0, 100, on_trackbar)
cv.createTrackbar('Red', 'Dreamy Glow Effect', 100, 200, on_trackbar) 
cv.createTrackbar('Blue', 'Dreamy Glow Effect', 100, 200, on_trackbar) 
cv.createTrackbar('Green', 'Dreamy Glow Effect', 100, 200, on_trackbar)

# Trackbars for contouring
cv.createTrackbar('Line Thickness', 'Dreamy Glow Effect', 1, 10, on_trackbar)
cv.createTrackbar('LineColor - R', 'Dreamy Glow Effect', 255, 255, on_trackbar)
cv.createTrackbar('LineColor - G', 'Dreamy Glow Effect', 255, 255, on_trackbar)
cv.createTrackbar('LineColor - B', 'Dreamy Glow Effect', 255, 255, on_trackbar)

while True:
    # Get trackbar positions for dreamy glow effect
    blur_strength = cv.getTrackbarPos('Blur', 'Dreamy Glow Effect')
    blend_strength = cv.getTrackbarPos('Blend', 'Dreamy Glow Effect') / 100.0
    red_value = cv.getTrackbarPos('Red', 'Dreamy Glow Effect')
    green_value = cv.getTrackbarPos('Green', 'Dreamy Glow Effect')
    blue_value = cv.getTrackbarPos('Blue', 'Dreamy Glow Effect')

    # Get trackbar positions for contouring
    contour_thickness = cv.getTrackbarPos('Line Thickness', 'Dreamy Glow Effect')
    contour_color = (
        cv.getTrackbarPos('LineColor - B', 'Dreamy Glow Effect'),
        cv.getTrackbarPos('LineColor - G', 'Dreamy Glow Effect'),
        cv.getTrackbarPos('LineColor - R', 'Dreamy Glow Effect')
    )

    # Apply the dreamy glow effect
    glowing_image = dreamy_glow_effect(final_result, blur_strength, blend_strength)

    # Adjust RGB values
    glowing_image = adjust_rgb(glowing_image, red_value, green_value, blue_value)

    # Apply contouring
    contour_image = apply_contours(glowing_image, contour_color, contour_thickness)

    # Display the updated image
    display_image('Dreamy Glow Effect', contour_image)

    # Wait for the user to press 'd' to exit
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

# Close all windows
cv.destroyAllWindows()
