import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Function to display an image
def display_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Convert to grayscale
def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize image
def resize_image(img, width, height):
    return cv2.resize(img, (width, height))

# Rotate image
def rotate_image(img, angle):
    (height, width) = img.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
    return rotated_img

# Crop image
def crop_image(img, start_x, start_y, end_x, end_y):
    return img[start_y:end_y, start_x:end_x]

# Apply Gaussian blur
def apply_gaussian_blur(img, kernel_size=(5, 5)):
    return cv2.GaussianBlur(img, kernel_size, 0)

# Save the image
def save_image(img, output_path):
    cv2.imwrite(output_path, img)

# Demonstration of the photo editor functions
def main():
    # 1. Display original image
    display_image('Original Image', image)

    # 2. Convert to grayscale
    gray_image = convert_to_grayscale(image)
    display_image('Grayscale Image', gray_image)

    # 3. Resize image
    resized_image = resize_image(image, 400, 400)  # Resize to 400x400
    display_image('Resized Image', resized_image)

    # 4. Rotate image (rotate 45 degrees)
    rotated_image = rotate_image(image, 45)
    display_image('Rotated Image', rotated_image)

    # 5. Crop image (crop to a region of interest)
    cropped_image = crop_image(image, 100, 100, 400, 400)  # Crop from (100, 100) to (400, 400)
    display_image('Cropped Image', cropped_image)

    # 6. Apply Gaussian blur
    blurred_image = apply_gaussian_blur(image, kernel_size=(7, 7))  # Use a 7x7 kernel
    display_image('Blurred Image', blurred_image)

    # 7. Save the final image (example saving resized image)
    save_image(resized_image, 'output_image.jpg')

# Run the program
if __name__ == '__main__':
    main()
