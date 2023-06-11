from src.data import DATA_DIR
import pysrt
from nltk.tokenize import word_tokenize
from collections import Counter
from src.utils import read_json, write_json


class Subtitle():

    def __init__(self, file_path):
        self.subs = pysrt.open(file_path)
        self.word = []

    def tokenizer(self):
        for line in self.subs:
            self.word.extend(word_tokenize(line.text.lower()))

    def get_difficult_words(self, word_diffculty_dict, difficulty_level):
        difficult_words = []
        for word in self.word:
            if word in word_diffculty_dict.keys():
                if word_diffculty_dict.get(word) > difficulty_level:
                    difficult_words.append(word)
        return difficult_words



if __name__ == "__main__":
    sub_file_path = DATA_DIR / 'src' / 'data' / \
        'Everybody Loves Raymond - 1x01 - Pilot.en.srt'
    difficult_file_path = DATA_DIR / 'src' / 'data' /  'word_diffculty.json'
    movie_name = Subtitle(sub_file_path)
    movie_name.tokenizer()
    # read difficulty dict
    difficult_dict = read_json(difficult_file_path)
    print(movie_name.get_difficult_words(difficult_dict, 3))