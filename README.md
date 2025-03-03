# Computer Vision: mini-projects

## Overview
This repository contains three Python scripts that apply various image processing techniques using **OpenCV**. These scripts allow users to perform different tasks such as basic image editing (grayscale, resizing, rotation, etc.), color segmentation, and applying artistic effects.

1. **Photo Editor Using Computer Vision**: Perform basic image processing operations like grayscale conversion, resizing, rotation, cropping, blurring, and saving images.
2. **K-Means Color Segmentation**: Segment an image into dominant color clusters using K-means clustering.
3. **Dreamy Glow Effect & Contour Enhancement**: Apply a dreamy glow effect and contour enhancement to an image, providing an interactive way to adjust parameters dynamically.

---

## Requirements  
Before running any of the scripts, ensure that you have the necessary dependencies installed:

```bash
pip install opencv-python numpy
```

---

## 1. Photo Editor Using Computer Vision  

### Overview  
This script applies basic image processing techniques such as **grayscale conversion, resizing, rotation, cropping, blurring, and saving images**. (I did this to to apply dreamy glow effect on photos initially, turns out it could work other ways too.)

### How Computer Vision is Used  
- **Grayscale conversion**: Converts the image to black and white.
- **Resizing**: Scales the image to different resolutions.
- **Rotation**: Rotates the image to adjust orientation.
- **Cropping**: Focuses on specific areas of the image.
- **Blurring**: Applies a blur effect to reduce image noise.

### Usage  
1. Place an image file named `image.jpg` in the same directory.
2. Run the script:  
   ```bash
   python PhotoEditor.py
   ```
3. The processed image will be displayed and saved as `output_image.jpg`.

### Conclusion  
This script demonstrates essential image processing techniques for use in computer vision-based applications.

---

## 2. K-Means Color Segmentation  

### Overview  
This script applies **K-means clustering** to segment an image into dominant color clusters. Users can adjust the number of clusters dynamically using a trackbar. (It could be useful for artists to simplify colour blocks or extract palette :D)

### How Computer Vision is Used  
- **K-means clustering** groups similar colors in the image.
- **Gaussian Blur** is applied to reduce noise before clustering.
- The script assigns each pixel to a dominant color cluster and displays the segmented image and the RGB values of the dominant colors.

### Usage  
1. Place an image named `sample.jpg` in the same directory.
2. Run the script:  
   ```bash
   python colorCode.py
   ```
3. A trackbar will appear, allowing you to adjust the number of color clusters (`K`).
4. The segmented image and dominant colors will be displayed.

### Conclusion  
This script is useful for **image color analysis, background simplification, and palette extraction** using computer vision.

---

## 3. Dreamy Glow Effect & Contour Enhancement  

### Overview  
This script applies a **dreamy glow effect** and **contour enhancement** to an image using **OpenCV**. Users can adjust parameters like **blur intensity, blending strength, RGB color balance, and contour thickness** through interactive trackbars. (The bounding box is square so it might look weird to you, I didn't want to fix it anymore. So, yea.)

### How Computer Vision is Used  
- **Gaussian blur** is applied to achieve the glow effect.
- **Bitwise masking** extracts the foreground.
- **Canny edge detection** is used for contouring to highlight edges.

### Usage  
1. Place an image named `image1.jpg` in the same directory.
2. Run the script:  
   ```bash
   python DreamyCutieEffect.py
   ```
3. Adjust the **blur, blend, RGB levels, and contour thickness** using the trackbars.
4. Press **'d'** to exit the script.

### Conclusion  
This script provides an interactive way to apply artistic effects like glowing and contour enhancement.

---



