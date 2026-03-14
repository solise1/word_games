import os, sys
import word_parser

if __name__ == '__main__':
    # Getting languages from files in raw dir
    filenames = os.listdir('raw')
    languages = list(map((lambda name: name.replace(".txt", "")), filenames))

    # Ensure output dirs exist
    if not os.path.exists('parsed/word_guesser'):
        os.makedirs('parsed/word_guesser')

    if not os.path.exists('parsed/general'):
        os.makedirs('parsed/general')

    # Second param in terminal, else default is 10
    max_len = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    # First param in terminal, else default is 5
    min_len = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    for language in languages:
        word_parser.WordParser.parse_for_word_guesser(language)
        word_parser.WordParser.parse_general(language, min_len, max_len)
