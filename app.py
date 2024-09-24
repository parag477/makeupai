import streamlit as st
import cv2
from makeup_app import MakeupApplication  # Your existing class
import numpy as np

# Initialize makeup application
makeup_app = MakeupApplication()

def main():
    st.title("Real-Time Virtual Makeup Application")

    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)

    stframe = st.empty()  # To display video frames

    if not cap.isOpened():
        st.error("Unable to access the camera.")
    else:
        st.success("Accessing the camera...")

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to capture frame from camera.")
            break

        # Apply virtual makeup to the frame
        frame = makeup_app.process_frame(frame)

        # Convert frame to RGB (OpenCV uses BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame
        stframe.image(frame, channels='RGB')

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

if __name__ == "__main__":
    main()
