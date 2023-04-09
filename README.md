# Topic Modeling

This repository contains example code for performing topic modeling on a corpus of text documents. The code is written in Python and uses the Gensim library for topic modeling.

### Installation
To use this code, you will need to have Python 3 installed on your computer. <br>
You can download Python from the official website: https://www.python.org/downloads/

You will also need to install the Gensim library.<br>
You can install it using pip, a package manager for Python. Open a terminal and run the following command:
```
pip install gensim
```

### Usage
The main file for performing topic modeling is **topic_modeling.py**.<br>
You can run it from the command line using the following command:
```
python topic_modeling.py <path-to-corpus>
```
Replace <path-to-corpus> with the path to your corpus of text documents.<br>
The corpus should be in plain text format, with one document per line.

The code will perform the following steps:

1- Load the corpus of text documents.<br>
2- Preprocess the documents by tokenizing, removing stop words, and stemming the words.<br>
3- Build a dictionary of all the unique words in the corpus.<br>
4- Build a bag-of-words representation of each document.<br>
5- Train a Latent Dirichlet Allocation (LDA) model using the bag-of-words representations.<br>
6- Print the top 10 topics and their most representative words.

### Example
To run the example code, clone this repository and navigate to the example directory.<br>
Then run the following command:
```
python topic_modeling.py corpus.txt
```

This will perform topic modeling on the corpus.txt file, which contains a collection of news articles. The output will show the top 10 topics and their most representative words.

### License
This code is licensed under the MIT License. See the LICENSE file for more information.
