#!/usr/bin/python3

import xml.etree.ElementTree as ET
import string

KLINGON_ASSISTANT_DIR = "klingon-assistant-data"

class Entry:
    def __init__(self, klingon, english):
        self.klingon = klingon
        self.english = english
        self.piqad = roman_to_piqad(self.klingon)
        self.type = ""
        self.notes = ""
        self.example = ""
        self.see_also = ""

    def make_piqad(self):
        self.piqad = roman_to_piqad(self.klingon)

    def to_latex_entry(self):
        # TODO add more
        entry = "\entry{" + self.klingon + "}
                        {" + self.piqad + "}
                        {" + self.type + "}
                        {" + self.english + "}
                        {" + self.notes + "}
                        {" + self.example + "}
                        {" + self.see_also + "}"
        return entry

    def sort_english(self):
        return self.english

def roman_to_piqad(roman_word):
    # Output the klingon unicode input for XeLaTeX (using "^^^^" before the unicode number)
    # Does NOT output xifan_hol nor direct pIqaD unicode
    return roman_word


def load_words_from_xml(filename}
    print(filename.split("-")[-1].split(".")[0])
    f = open(filename, "")



    pass





# First pass: one by one, go through each letter, output latex file for klingon entries, generate Tlh-Eng chapter

language_filename_list = ["file1", "file2", "file3"]

letters = list(string.ascii_lowercase)
entries = {}

for l in letters:
    entries[l] = []


for filename in language_filename_list:
    # open file
    letter = filename.split("-")[-1].split(".")[0]
    words = load_words_from_xml(filename)

    latex_output = ""

    for word in words:

        # Add entry to current running output
        latex_output = latex_output + word.to_latex_entry() + '\n'
        entries[word.english[0]].append(word)

    # write out latex output
    new_filename = "latex/entries_"+letter+".tex"
    f = open(new_filename, "x")
    f.write(latex_output)
    f.close


# Second pass: use recorded english entries to generate Eng-Tlh chapter
"""
