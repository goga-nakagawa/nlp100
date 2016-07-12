#!/usr/bin/env python
# -*- coding: utf-8 -*-

def createDict(s):
    res = {}
    for index, word in enumerate(s.split()):
        if index + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            res[word[:1]] = index + 1
        else:
            res[word[:2]] = index + 1
    return res

print createDict("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")