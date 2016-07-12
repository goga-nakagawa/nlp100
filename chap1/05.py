#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(s, n):
    res = []
    for index, char in enumerate(s):
        if index + n <= len(s):
            res.append(s[index:index+n])
    return res

print ngram("I am an NLPer", 2)
