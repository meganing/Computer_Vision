import cv2
import numpy as np
import os

# Function to detect and compute keypoints and descriptors using ORB
def detect_features(image):
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors

# Function to match features using BFMatcher
def match_features(des1, des2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    return matches

# Function to extract match count as a classification feature
def get_match_count(matches):
    return len(matches)

# Function to classify image based on matching with reference images
def classify_image(input_image, reference_images):
    # Convert the input image to grayscale
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    
    # Initialize a dictionary to store the match counts for each reference image
    match_counts = {}

    # Loop through each reference image, calculate matches, and store the count
    for label, ref_image in reference_images.items():
        # Convert reference image to grayscale
        ref_gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)

        # Detect keypoints and descriptors for both input and reference image
        kp1, des1 = detect_features(input_gray)
        kp2, des2 = detect_features(ref_gray)

        # Match features between the input image and the reference image
        matches = match_features(des1, des2)

        # Get the match count as the classification feature
        match_count = get_match_count(matches)

        # Store the match count for the reference image
        match_counts[label] = match_count

    # Classify the image based on the reference image with the highest match count
    best_match_label = max(match_counts, key=match_counts.get)
    return best_match_label, match_counts

# Load your reference images into a dictionary (as the template images)
# You can add as many reference images as you want
reference_images = {
    'class_1': cv2.imread('img3.jpg'),
    'class_2': cv2.imread('darwin.jpg'),
    'class_3': cv2.imread('RCW.jpg')
}


# Load the input image you want to classify
input_image = cv2.imread('img6.jpg')

# Perform image classification based on feature matching
label, match_counts = classify_image(input_image, reference_images)

# Print the classification result
print(f"Classified as: {label}")
print("Match Counts for each class:", match_counts)

# Visualize the result
cv2.imshow('Input Image', input_image)

# Display the reference images
for label, ref_image in reference_images.items():
    cv2.imshow(f'Reference Image - {label}', ref_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
