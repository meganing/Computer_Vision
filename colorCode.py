import cv2 as cv
import numpy as np

# Function to display the image and color codes
def display_colors(colors, image, k):
    # Display the original image
    cv.imshow('Original Image', image)
    
    cluster_image = np.zeros((200, 120 * k, 3), dtype=np.uint8)
    
    for i in range(k):
        cluster_image[:, i * 120:(i + 1) * 120] = colors[i]
    
    # Display the segmented colors in the cluster image
    cv.imshow('Color Clusters', cluster_image)
    
    # Print the RGB values of each cluster center (dominant color)
    print(f"\nDominant Colors (RGB values) - Number of clusters: {k}")
    for i in range(k):
        print(f"Color {i + 1}: RGB = {colors[i]}")

# Function to perform K-means clustering on the image
def kmeans_image_segmentation(image, k=3):
    # Preprocess the image to reduce noise using Gaussian Blur
    preprocessed_image = cv.GaussianBlur(image, (5, 5), 0)
    
    # Reshape the image into a 2D array of pixels
    pixel_data = preprocessed_image.reshape((-1, 3))
    
    # Convert to float32 for K-means
    pixel_data = np.float32(pixel_data)
    
    # Define criteria and apply KMeans
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv.kmeans(pixel_data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    
    # Convert centers back to uint8
    centers = np.uint8(centers)
    
    # Assign each pixel to the nearest cluster center
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    
    return segmented_image, labels, centers

# Callback function for the trackbar
def on_trackbar(val):
    k = val
    segmented_image, labels, centers = kmeans_image_segmentation(img, k)
    display_colors(centers, img, k)

# Load the image
img = cv.imread('sample.jpg')  
if img is None:
    print("Error: Could not load the image. Please check the file path.")
    exit()

# Create windows and track bar
cv.namedWindow('K-means Color Segmentation')
cv.createTrackbar('K (Clusters)', 'K-means Color Segmentation', 3, 10, on_trackbar)

# Initial segmentation with k=3
on_trackbar(3)

# Wait for the user to press a key and close all windows
cv.waitKey(0)
cv.destroyAllWindows()