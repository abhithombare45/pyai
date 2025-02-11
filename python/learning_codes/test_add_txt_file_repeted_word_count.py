import pandas as pd
import numpy as np


def main():
    words = pd.read_txt(
        "/Users/abhijeetthombare/vscode/python/learning_codes/address.txt"
    )
    lowercase_words = [word.lower() for word in words if len(word) >= 4]
    counts = {word: words.count(word) for word in lowercase_words}
    save.counts(counts)


print("Abhi")
main()
print(counts)
