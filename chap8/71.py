#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stop_words import get_stop_words

def is_stop_words(word):
    return word.strip().lower() in get_stop_words("en")

with open("rt-polarity.pos") as f:
    for l in f.readlines():
        for w in l.replace(",", "").replace(".","").split():
            print "%s is%s a stop_word." % (w, "" if is_stop_words(w) else " not")