# NLP Named Entity Recognition (NER) Application
<img src="https://www.rosette.com/wp-content/uploads/2022/03/header-img-event-extraction@2x.png" >
This is a Python application for Named Entity Recognition (NER) using the SpaCy library. NER is a subtask of Natural Language Processing (NLP) that aims to identify and classify named entities in text into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

This application provides a simple and efficient way to extract named entities from text data, allowing you to gain insights from unstructured textual data and automate various tasks such as information extraction, question answering, document classification, and more.

## Features
- **Named Entity Recognition:** Identify and classify named entities in text data.
- **Pretrained Models:** Utilize SpaCy's pretrained models for different languages.
- **Customization:** Fine-tune or train your own models for specific domains or languages.
- **Efficient Processing:** Process large amounts of text data quickly and accurately.
- **Flexible Output:** Obtain the recognized entities along with their labels and positions in the text.
- **Easy Integration:** Integrate the NER functionality into your own Python projects.

## Usage
### Step 1:
```
export PYTHONPATH=${PWD}

```
### Step 2:
Create environment and install requierments in your system
```
pip install -r requirenments.txt

```
### Step 3:
Download en_core_web_sm package
```
python -m spacy download en_core_web_sm

```
### Step 4:
Run streamlit web app
```
streamlit run src/app/demo.py 

```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Conclusion

The NLP Named Entity Recognition (NER) Application provides an easy-to-use solution for extracting named entities from text data. By leveraging the power of SpaCy, you can quickly identify and classify entities in various languages. Whether you need to perform information extraction, document classification, or any other task that involves identifying named entities, this application is a great starting point for your NLP projects.
