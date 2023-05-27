import streamlit as st
from src.youtube_downloader import YouTubeDownoader
from src.utils import download_transcript


st.header('YouTube Downloader')
st.image('https://responsivechecker.net/images/youtube-downloader.png')
url = st.text_input('Enter YouTube Video URL:')
options = st.selectbox(
    'Downloads Options:',
    ['Video', 'Audio', 'Trancript Persian', 'Trancript English', 'All'])

button = st.button('Generate')

obj = YouTubeDownoader(url)

if button:
    if options == 'Video':
        obj.download_video('src/data')
    elif options == 'Audio':
        obj.download_audio('src/data')
    elif options == 'Trancript Persian':
        text = obj.get_transcript(return_lang='fa')
        st.write(text)
        download_transcript(st)
    elif options == 'Trancript English':
        text = obj.get_transcript()
        st.write(text)
        download_transcript(text)