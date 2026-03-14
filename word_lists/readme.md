# WordParser

Parses word lists and outputs new lists for word guesser and for other games.

## Usage
Inside this folder, run:

```shell
python parse_all.py
```

You can optionally specify the minimum and maximum (exclusive) amount of letters to override the defaults (5 and 10):

```shell
python parse_all.py 4 7
```

Output can be found in:

`/parsed/word_guesser` (contains only 5 letter words)

`/parsed/general` (contains any words that are the appropriate length for general games)

## Adding new languages

To add a new language, just add a new .txt file with the name of the language (say, french.txt) with the list of words you want and simply parse again.

## Attribution

Word lists in `/raw` obtained from https://github.com/bukowa/1000-common-words/tree/master
