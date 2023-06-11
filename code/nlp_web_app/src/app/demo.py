import streamlit as st
# import soundfile as sf
from src.ner import build_entity
from src.speech2transcript import audio_to_transcript
from src.utils import save_transcript, download_link_transcript, read_text
from src.wordcloud_generator import create_wordcloud
from src.summarize_text import summarize_BART


import streamlit as st

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: transparent;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



# Name Entity
st.image("https://www.rosette.com/wp-content/uploads/2022/03/header-img-event-extraction@2x.png")
st.header('Find Named Entitiy')


## upload text file for ENT
uploaded_file = st.file_uploader("**Upload an text file**")

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the contents of the file as a string
    text = uploaded_file.read().decode('utf-8')

    # Display the uploaded file's contents
    st.success("Uploaded text")

else:
    st.error("No file uploaded.")


options = st.multiselect(
    '**What do you want to generate?**',
    ['NER', 'Wordcloud', 'Summarization', 'Topic'],
    ['NER'])
gen_button = st.button('Generate')

if 'NER' in options and gen_button == True:
    st.markdown('### NER')
    st.dataframe(build_entity(text))

if 'Wordcloud' in options and gen_button == True:
    st.markdown('### Wordcloud')
    # Create the word cloud figure
    fig_buffer = create_wordcloud(text, max_words=50, colormap='cool', background_color='lightgrey')

    # Display the figure in Streamlit
    st.image(fig_buffer, use_column_width=True)

if 'Summarization' in options and gen_button == True:
    st.markdown('### Summarization')
    summarize_text = summarize_BART(text)
    st.write(summarize_text)

if 'Topic' in options and gen_button == True:
    st.markdown('### Topic')