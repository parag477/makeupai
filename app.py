import streamlit as st
import cv2
import numpy as np

st.title("Real-Time Virtual Makeup")

# Initialize OpenCV for video capture
cap = cv2.VideoCapture(0)  # '0' is the default camera

if not cap.isOpened():
    st.error("Error: Could not open video stream.")
else:
    st.write("Camera opened successfully!")

# Frame window
frame_placeholder = st.empty()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to grab frame from camera.")
            break

        # Optionally, apply your makeup effects here using OpenCV.
        # For demonstration, we'll convert it to grayscale.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert the frame to RGB for displaying in Streamlit
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in Streamlit
        frame_placeholder.image(rgb_frame, channels="RGB")

except Exception as e:
    st.error(f"Error: {e}")

# Release the camera resource
cap.release()
