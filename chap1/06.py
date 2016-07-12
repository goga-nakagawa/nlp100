#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bigram(s):
    res = set()
    for index, char in enumerate(s):
        if index + 2 <= len(s):
            res.add(s[index:index+2])
    return res

def unionbigrams(s1, s2):
    return bigram(s1).union(bigram(s2))

def intersectionbigrams(s1, s2):
    return bigram(s1).intersection(bigram(s2))

def difbigrams(s1, s2):
    return bigram(s1).difference(bigram(s2))

def isIncludedIn(target, s):
    return target in bigram(s)


print unionbigrams("paraparaparadise", "paragraph")
print intersectionbigrams("paraparaparadise", "paragraph")
print difbigrams("paraparaparadise", "paragraph")

print isIncludedIn("se", "paraparaparadise")
print isIncludedIn("se", "paragraph")
