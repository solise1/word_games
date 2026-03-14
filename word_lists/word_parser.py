class WordParser():
    @staticmethod
    def parse_for_word_guesser(language):
        WordParser(5, 5, f'raw/{language}.txt', f'parsed/word_guesser/{language}.txt').parse()

    @staticmethod
    def parse_general(language, min_len, max_len):
        WordParser(min_len, max_len, f'raw/{language}.txt', f'parsed/general/{language}.txt').parse()

    def __init__(self, min_len, max_len, words_file, save_to):
        self.min_len = min_len
        self.max_len = max_len
        self.words = open(words_file, 'r').read().split('\n')
        self.save_to = save_to

    def parse(self):
        valid_words = []
        for word in self.words:
            if len(word) >= self.min_len and len(word) <= self.max_len:
                valid_words.append(word)
        with open(self.save_to, 'w') as f:
            f.write('\n'.join(valid_words))

    # * Wrote before deciding on just using .txt files,
    # * but it might be useful to somebody else!
    # * Make sure to import yaml if using this
    def parse_as_yaml(self):
        indexes = range(self.min_len, self.max_len)
        word_dict = {index: [] for index in indexes}
        for word in self.words:
            if len(word) >= self.min_len and len(word) <= self.max_len:
                word_dict[len(word)].append(word)
        with open(self.save_to, 'w') as f:
            yaml.dump(word_dict, f)
