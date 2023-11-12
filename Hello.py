import streamlit as st
from streamlit.logger import get_logger
from st_files_connection import FilesConnection
import s3fs

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋"
    )

    # Create S3 file system object
    s3 = s3fs.S3FileSystem()

    # Read current content from S3
    with s3.open("streamlitgreetingscard/greetings.txt", "r") as file:
        current_content = file.read()
        st.write(current_content)

    # Play audio if file is uploaded
    with s3.open("streamlitgreetingscard/audio_file.mp3", "rb") as audio_file:
        audio_content = audio_file.read()
        st.audio(audio_content, format='audio/mp3', start_time=0)


    

if __name__ == "__main__":
    run()