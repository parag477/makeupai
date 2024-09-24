import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import cv2
import av

class VirtualMakeupProcessor(VideoProcessorBase):
    def __init__(self):
        # Initialize any necessary variables here
        pass

    def recv(self, frame):
        # Check if the frame is valid
        if frame is None:
            st.error("Received an empty frame.")
            return None

        try:
            # Convert the frame to a numpy array for OpenCV
            img = frame.to_ndarray(format="bgr24")
            
            # Example: Apply makeup processing here
            img = self.process_frame(img)  # Replace with your processing function
            
            # Return the processed frame
            return av.VideoFrame.from_ndarray(img, format="bgr24")
        except Exception as e:
            st.error(f"Error processing video: {e}")
            return frame  # Return the original frame if processing fails

    def process_frame(self, img):
        # Implement your makeup application logic here
        return img  # Modify this to return the processed image

st.title("Virtual Makeup Application - Real-time Camera Access")

# Start the webcam stream using WebRTC
webrtc_ctx = webrtc_streamer(
    key="makeup-app",
    video_processor_factory=VirtualMakeupProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

if webrtc_ctx.state.playing:
    st.write("Camera is active!")
