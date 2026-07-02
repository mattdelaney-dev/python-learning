# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "nato_phonetic_alphabet.csv")

data = pandas.read_csv(file_path)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()