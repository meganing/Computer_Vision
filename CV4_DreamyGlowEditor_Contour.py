import cv2 as cv
import numpy as np

# Load the face cascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to apply the dreamy glow effect
def dreamy_glow_effect(img, blur_strength, blend_strength):
    if blur_strength % 2 == 0:
        blur_strength += 1
    blurred_image = cv.GaussianBlur(img, (blur_strength, blur_strength), 0)
    glowing_image = cv.addWeighted(img, 1 - blend_strength, blurred_image, blend_strength, 0)
    return glowing_image

# Function to adjust RGB values
def adjust_rgb(img, red_value, green_value, blue_value):
    adjusted_image = img.copy()
    bluefactor = blue_value / 100.0
    greenfactor = green_value / 100.0
    redfactor = red_value / 100.0
    adjusted_image[:, :, 0] = np.clip(adjusted_image[:, :, 0] * bluefactor, 0, 255)
    adjusted_image[:, :, 1] = np.clip(adjusted_image[:, :, 1] * greenfactor, 0, 255)
    adjusted_image[:, :, 2] = np.clip(adjusted_image[:, :, 2] * redfactor, 0, 255)
    return adjusted_image

# Function to apply contours
def apply_contours(img, contour_color, contour_thickness):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150)
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv.drawContours(contour_img, contours, -1, contour_color, contour_thickness)
    return contour_img

# Callback function for the trackbars
def on_trackbar(val):
    pass

# Initialize video capture
cap = cv.VideoCapture('video.mp4')

# Create a window for trackbars
cv.namedWindow('Face Tracking with Dreamy Glow')

# Trackbars for dreamy glow effect
cv.createTrackbar('Blur', 'Face Tracking with Dreamy Glow', 1, 100, on_trackbar)
cv.createTrackbar('Blend', 'Face Tracking with Dreamy Glow', 0, 100, on_trackbar)
cv.createTrackbar('Red', 'Face Tracking with Dreamy Glow', 100, 200, on_trackbar)
cv.createTrackbar('Blue', 'Face Tracking with Dreamy Glow', 100, 200, on_trackbar)
cv.createTrackbar('Green', 'Face Tracking with Dreamy Glow', 100, 200, on_trackbar)

# Trackbars for contouring
cv.createTrackbar('Line Thickness', 'Face Tracking with Dreamy Glow', 1, 10, on_trackbar)
cv.createTrackbar('LineColor - R', 'Face Tracking with Dreamy Glow', 255, 255, on_trackbar)
cv.createTrackbar('LineColor - G', 'Face Tracking with Dreamy Glow', 255, 255, on_trackbar)
cv.createTrackbar('LineColor - B', 'Face Tracking with Dreamy Glow', 255, 255, on_trackbar)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    blur_strength = cv.getTrackbarPos('Blur', 'Face Tracking with Dreamy Glow')
    blend_strength = cv.getTrackbarPos('Blend', 'Face Tracking with Dreamy Glow') / 100.0
    red_value = cv.getTrackbarPos('Red', 'Face Tracking with Dreamy Glow')
    green_value = cv.getTrackbarPos('Green', 'Face Tracking with Dreamy Glow')
    blue_value = cv.getTrackbarPos('Blue', 'Face Tracking with Dreamy Glow')
    contour_thickness = cv.getTrackbarPos('Line Thickness', 'Face Tracking with Dreamy Glow')
    contour_color = (
        cv.getTrackbarPos('LineColor - B', 'Face Tracking with Dreamy Glow'),
        cv.getTrackbarPos('LineColor - G', 'Face Tracking with Dreamy Glow'),
        cv.getTrackbarPos('LineColor - R', 'Face Tracking with Dreamy Glow')
    )

    # Process each detected face
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = frame[y:y+h, x:x+w]

        # Apply the dreamy glow effect and RGB adjustment
        glowing_face = dreamy_glow_effect(face_roi, blur_strength, blend_strength)
        glowing_face = adjust_rgb(glowing_face, red_value, green_value, blue_value)

        # Apply contouring effect on the face
        glowing_face = apply_contours(glowing_face, contour_color, contour_thickness)

        # Place the modified face back onto the frame
        frame[y:y+h, x:x+w] = glowing_face

    # Display the updated frame
    cv.imshow('Face Tracking with Dreamy Glow', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
