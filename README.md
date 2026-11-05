# text-statistics-cli

Count words, lines, characters and frequent words in UTF-8 text.

Maintained by @arjunkapoorkapadiya-rgb.

## Requirements

Python 3.9 or newer. No third-party dependencies.

## Quick start

Run from this repository's directory:

    python main.py sample.txt --top 5

A sample input file is included.

## Behavior and limitations

Reads UTF-8 text into memory. Counts case-insensitive word tokens, including numbers and internal apostrophes. This is a simple tokenizer, not language-aware word segmentation. Character counts use decoded text with normalized newlines. Outputs JSON. Exit code 2 indicates invalid input.