import io
from collections import Counter

import matplotlib.pyplot as plt
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud


def create_wordcloud(text_data, max_words=100, input_stopwords=None, colormap='viridis', background_color='black', width=800, height=400):
    # Tokenize the text data
    tokens = word_tokenize(text_data)

    # Remove stopwords
    if input_stopwords is None:
        stopwords_set = set(stopwords.words('english'))
    tokens = [token.lower() for token in tokens if token.lower() not in stopwords_set]

    # Count word frequencies
    word_freq = Counter(tokens)

    # Generate the word cloud
    wordcloud = WordCloud(width=width, height=height, max_words=max_words, colormap=colormap, background_color=background_color).generate_from_frequencies(word_freq)

    # Create a buffer to store the image
    fig_buffer = io.BytesIO()

    # Save the word cloud figure to the buffer
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(fig_buffer, format='png')
    plt.close()

    # Return the figure buffer
    return fig_buffer