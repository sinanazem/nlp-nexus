import base64
import json

import streamlit as st


def save_transcript(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)



def download_link_transcript(file_data):

    # Create a download link
    b64_file = base64.b64encode(file_data.encode()).decode()
    download_link = f'<a href="data:application/octet-stream;base64,{b64_file}" download="file.txt">Download File</a>'

    # Display the download button
    st.markdown(download_link, unsafe_allow_html=True)

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.read()


def write_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data