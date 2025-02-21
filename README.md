<h1>INTRO</h1>
<h3>The INVISO project is an innovative application of computer vision and image processing techniques using OpenCV. Inspired by the concept of Harry Potter’s invisibility cloak, this project leverages color detection and segmentation to create a real-time visual illusion where any specific colored object appears invisible by replacing it with the background.

By utilizing a single-color detection (such as green, red, or blue), the system detects and masks the target object's color pixels in a video stream, seamlessly overlaying them with the captured background. This effect is achieved by processing frames in the HSV color space, applying bitwise operations, and refining the output with morphological transformations to remove noise and improve accuracy.

This project is a fascinating blend of computer vision, image processing, and real-time video manipulation, making it an engaging learning experience for those interested in machine learning, artificial intelligence, and OpenCV-based projects. Through the implementation of color thresholding, masking, and background replacement techniques, this project demonstrates the power of OpenCV in real-world applications.

</h3>

<h1>TECH STACK USED📲📲</h1>
<h3>🐍Python – 3.x</h3>
<h3>🎲Numpy</h3>
<h3>👾OpenCV</h3>
<h3>💻Streamlit</h3>

<h1>IMPLEMENTATION👩🏼‍💻</h1>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Code Explanation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 20px;
            padding: 20px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        .section {
            background: white;
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .code {
            background: #2d2d2d;
            color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            font-family: "Courier New", monospace;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>

  <h1>📌 INVISO: Code Explanation</h1>
    <p>This document explains the working of the <b>INVISO</b> project, which makes a selected color disappear using OpenCV and Streamlit.</p>

  <div class="section">
        <h2>1️⃣ Importing Necessary Packages</h2>
        <p>The following libraries are imported:</p>
        <div class="code">
            import cv2 <br>
            import time <br>
            import numpy as np <br>
            import streamlit as st
        </div>
        <p><b>Explanation:</b> These libraries handle video processing (<b>cv2</b>), time delays (<b>time</b>), numerical computations (<b>numpy</b>), and web-based UI (<b>streamlit</b>).</p>
    </div>

  <div class="section">
        <h2>2️⃣ UI Setup with Streamlit</h2>
        <p>The web interface displays a title and a dropdown for selecting the color to disappear.</p>
        <div class="code">
            st.title("INVISO") <br>
            st.write("Select the color that you want to disappear") <br>
            selected_color = st.selectbox("Choose Cloak Color", list(color_options.keys()))
        </div>
    </div>

  <div class="section">
        <h2>3️⃣ Defining Color Ranges</h2>
        <p>The program allows users to select a color that will be removed using a color range in the HSV format.</p>
        <div class="code">
            color_options = { "Green": ([50, 80, 50], [90, 255, 255]), "Red": ([0, 120, 70], [10, 255, 255]), ... }
        </div>
        <p>Each color has an HSV range, where lower and upper bounds define its shade.</p>
    </div>

  <div class="section">
        <h2>4️⃣ Capturing Background</h2>
        <p>The webcam captures the background before the effect starts.</p>
        <div class="code">
            cap = cv2.VideoCapture(0) <br>
            time.sleep(2) <br>
            _, background = cap.read() <br>
        </div>
        <p>The program waits for 2 seconds before capturing the background twice.</p>
    </div>

  <div class="section">
        <h2>5️⃣ Noise Removal with Morphological Operations</h2>
        <p>The following kernels help in filtering the mask:</p>
        <div class="code">
            open_kernel = np.ones((5, 5), np.uint8)  # Removes noise <br>
            close_kernel = np.ones((7, 7), np.uint8)  # Fills holes <br>
            dilation_kernel = np.ones((10, 10), np.uint8)  # Expands mask <br>
        </div>
    </div>

  <div class="section">
        <h2>6️⃣ Processing the Video Stream</h2>
        <p>The program continuously reads video frames and applies the disappearing effect.</p>
        <div class="code">
            while cap.isOpened(): <br>
            &nbsp;&nbsp;&nbsp;&nbsp; ret, frame = cap.read() <br>
            &nbsp;&nbsp;&nbsp;&nbsp; if not ret or stop: break <br><br>

  &nbsp;&nbsp;&nbsp;&nbsp; hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) <br>
            &nbsp;&nbsp;&nbsp;&nbsp; mask = cv2.inRange(hsv, lower_bound, upper_bound) <br>
            &nbsp;&nbsp;&nbsp;&nbsp; mask = filter_mask(mask) <br>
        </div>
        <p>The color mask is applied to detect the selected color.</p>
    </div>

  <div class="section">
        <h2>7️⃣ Creating the Invisible Effect</h2>
        <p>The program replaces the detected color with the previously captured background.</p>
        <div class="code">
            cloak = cv2.bitwise_and(background, background, mask=mask) <br>
            inverse_mask = cv2.bitwise_not(mask) <br>
            current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask) <br>
            combined = cv2.add(cloak, current_background) <br>
            frame_placeholder.image(combined, channels="BGR") <br>
        </div>
        <p>This creates an illusion of invisibility by blending the background.</p>
    </div>

  <div class="section">
        <h2>8️⃣ Stopping the Video Capture</h2>
        <p>When the user stops the effect, the program releases the webcam.</p>
        <div class="code">
            cap.release() <br>
            cv2.destroyAllWindows()
        </div>
        <p>The webcam stream is properly closed to free system resources.</p>
    </div>

  <h2>✅ Conclusion</h2>
    <p>The INVISO project creates a real-time invisibility cloak effect using OpenCV. It replaces a selected color with the captured background, making it look like the object has disappeared.</p>

</body>
</html>

