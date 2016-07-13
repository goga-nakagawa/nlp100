#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle

def typoglycemia(s):
    words = s.split()
    res = []
    for word in words:
        if len(word) <= 4:
            res.append(word)
        else:
            mid = list(word[1:-1])
            shuffle(mid)
            res.append(word[0] + "".join(mid) + word[-1])
    return " ".join(res)



print typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")