#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from nltk import stem

ls = re.compile(r"^\n")
st = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")

class Stemmer:
    def __init__(self, stemmer=None):
        self.stemmer = stem.PorterStemmer()

    def stem(self, word):
        return self.stemmer.stem(word.lower())


with open("nlp.txt") as f:
    for l in f.readlines():
        if ls.match(l):
            continue
        else:
            sentences = st.split(l)
            for s in sentences:
                for w in s.split():
                    stemmer = Stemmer()
                    if w[-1] == ".":
                        print stemmer.stem(w.replace(".", ""))
                        print ""
                    elif w[-1] == ",":
                        print stemmer.stem(w.replace(",", ""))
                    else:
                        print stemmer.stem(w)

