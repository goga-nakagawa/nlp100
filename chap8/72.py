#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from stop_words import get_stop_words
from nltk.stem import PorterStemmer

pol = re.compile(r"^(\+1\s|\-1\s)(.*?)\n$")
word = re.compile(r"[,.:;\s]")

base_features = []

def is_stop_words(word):
    return word.strip().lower() in get_stop_words("en")


with open("sentiment.txt") as f:
    for l in f.readlines():
        sent = pol.match(l)
        if sent:
            polarity = sent.group(1).strip()
            sentence = sent.group(2).strip()
            words = word.split(sentence)
            for w in words:
                if not is_stop_words(w) and w:
                    try:
                        base_features.append(PorterStemmer().stem(w))
                    except UnicodeDecodeError:
                        # case when w has not alphabetic character
                        continue
print base_features
