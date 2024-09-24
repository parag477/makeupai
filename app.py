import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import cv2
import av
from makeup_app import MakeupApplication  # Assuming you have a class for processing

class VirtualMakeupProcessor(VideoProcessorBase):
    def recv(self, frame):
        try:
            img = frame.to_ndarray(format="bgr24")
            # Apply makeup processing here
            return av.VideoFrame.from_ndarray(img, format="bgr24")
        except Exception as e:
            st.error(f"Error in video processing: {e}")
            return frame



st.title("Virtual Makeup Application - Real-time Camera Access")

# Start the webcam stream using WebRTC
webrtc_ctx = webrtc_streamer(
    key="makeup-app",
    video_processor_factory=VirtualMakeupProcessor,
    media_stream_constraints={
        "video": {
            "width": {"ideal": 640},  # Lower the resolution
            "height": {"ideal": 480}
        },
        "audio": False
    },
    async_processing=True,
)


if webrtc_ctx.state.playing:
    st.write("Camera is active.")
    st.write("State: Playing")
else:
    st.write(f"Current state: {webrtc_ctx.state}")

