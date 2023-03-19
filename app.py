import streamlit as st
import whisper

st.title("Holocaust Oral Testimony Analysis")

# upload audio file
audio_file = st.file_uploader("upload Audio", type=["wav", "mp3", "mp4"])
path = '/home/isuri/Desktop/sample_video'

username = st.text_input('Insert username')
st.write(username)

password = st.text_input('Insert password')
st.write(password)

model = whisper.load_model("tiny")
st.sidebar.success("Whisper model Loaded")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])

        with open("audio_sample.txt", "w+") as f:
            f.write(transcription["text"])

    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header('Play Original Audio File')
st.sidebar.audio(audio_file)

