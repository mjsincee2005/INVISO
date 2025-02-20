import cv2
import time
import numpy as np
import streamlit as st

st.title("Invisibility Cloak using OpenCV")
st.write("Select the color of the cloak you want to disappear")
st.write("To test the invisiblilty")

# Define color options
color_options = {
    "Green": ([50, 80, 50], [90, 255, 255]),
    "Red": ([0, 120, 70], [10, 255, 255]),
    "Blue": ([100, 150, 0], [140, 255, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255]),
    "Cyan": ([80, 100, 100], [100, 255, 255]),
    "Magenta": ([140, 100, 100], [170, 255, 255]),
    "Orange": ([10, 150, 150], [25, 255, 255]),
    "Purple": ([125, 100, 100], [150, 255, 255]),
    "Pink": ([160, 100, 100], [180, 255, 255]),
    "White": ([0, 0, 200], [180, 30, 255])
}

# User selects color
selected_color = st.selectbox("Choose Cloak Color", list(color_options.keys()))
lower_bound, upper_bound = map(np.array, color_options[selected_color])

start = st.button("Start Cloak Effect")
stop = st.button("Stop Cloak Effect")

if start:
    cap = cv2.VideoCapture(0)
    
    st.write("Capturing background... Please wait")
    time.sleep(2)
    _, background = cap.read()
    time.sleep(2)
    _, background = cap.read()
    
    open_kernel = np.ones((5, 5), np.uint8)
    close_kernel = np.ones((7, 7), np.uint8)
    dilation_kernel = np.ones((10, 10), np.uint8)
    
    def filter_mask(mask):
        close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
        open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, open_kernel)
        dilation = cv2.dilate(open_mask, dilation_kernel, iterations=1)
        return dilation
    
    frame_placeholder = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or stop:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        mask = filter_mask(mask)
        cloak = cv2.bitwise_and(background, background, mask=mask)
        inverse_mask = cv2.bitwise_not(mask)
        current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)
        combined = cv2.add(cloak, current_background)
        
        frame_placeholder.image(combined, channels="BGR")
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()



