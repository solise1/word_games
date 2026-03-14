import random

from word_games.settings import BASE_DIR

class WordGuesser():
    def __init__(self, language):
        self.language = language

    def pick_random(self):
        return random.choice(self.load_word_list())

    def load_word_list(self):
        with open(f'{BASE_DIR}/word_lists/parsed/word_guesser/{self.language}.txt', 'r') as f:
            return f.read().split("\n")
