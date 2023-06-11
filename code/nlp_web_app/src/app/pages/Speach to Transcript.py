import streamlit as st
# import soundfile as sf
from src.ner import build_entity
from src.speech2transcript import audio_to_transcript
from src.utils import save_transcript, download_link_transcript
from src.app.st_custom_components import st_audiorec

# Speech to Transcript
#st.image('https://www.rev.com/blog/wp-content/uploads/2019/04/Rev-HowtoParaphraseAudio.gif')
st.image('https://www.paradiso.ai/wp-content/uploads/2023/01/speech-to-text-4.png')
# st.image('https://www.rev.com/blog/wp-content/uploads/2020/12/2020.11_Marketing_BlogHeaders_Nov30_AM_Artboard-1-copy-5-1024x576.jpg')
st.header('Speach to Transcript')


uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    audio_data = uploaded_file.getvalue()
    try:
        with open("src/data/file.m4a", "wb") as f:
            f.write(audio_data)
        st.success("Audio file saved successfully!")
        transcript = audio_to_transcript("src/data/file.m4a")
        download_link_transcript(transcript)

    except FileNotFoundError:
        transcript = ''

st.markdown('## Voice')

# import streamlit as st
# from audio_recorder_streamlit import audio_recorder

# audio_bytes = audio_recorder()
# if audio_bytes:
#     st.audio(audio_bytes, format="audio/wav")

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # display audio data as received on the backend
    st.audio(wav_audio_data, format='audio/wav')