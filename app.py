import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile

st.title("MoviePy with Streamlit")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    st.video(temp_file_path)

    if st.button("Extract Audio"):
        video = VideoFileClip(temp_file_path)
        audio = video.audio

        audio_output_path = temp_file_path + ".mp3"
        audio.write_audiofile(audio_output_path)

        st.audio(audio_output_path, format='audio/mp3')
        st.success("Audio extracted successfully!")