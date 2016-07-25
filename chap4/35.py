#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from itertools import izip
pattern = r"\t|\,"
compiled = re.compile(pattern)

with open('neko.txt.mecab') as f:
    result = [[]]
    lines = f.readlines()
    for curr, next in izip(lines[:], lines[1:]):
        curr_matched = compiled.split(curr)
        next_matched = compiled.split(next)
        if len(curr_matched) == 10 and len(next_matched) == 10:
            if curr_matched[1] != "名詞" and\
               next_matched[1] == "名詞":
                result.append([next_matched[0]])
            elif curr_matched[1] == "名詞" and\
               next_matched[1] == "名詞":
                result[-1].extend(next_matched[0])

    for r in result:
        print ''.join(r).decode('utf-8')
