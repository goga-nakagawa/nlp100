#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from nltk import tokenize

ls = re.compile(r"^\n")
st = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")

with open("nlp.txt") as f:
    for l in f.readlines():
        if ls.match(l):
            continue
        else:
            sentences = st.split(l)
            for s in sentences:
                for w in tokenize.word_tokenize(s):
                    if w == ".":
                        print ""
                        continue
                    elif w == ",":
                        continue
                    elif w == "(":
                        continue
                    elif w == ")":
                        continue
                    else:
                        print w


