#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from itertools import izip
pattern = r"\t|\,"
compiled = re.compile(pattern)

with open('neko.txt.mecab') as f:
    lines = f.readlines()
    for curr, next, nextnext in izip(lines[:], lines[1:], lines[2:]):
        curr_matched = compiled.split(curr)
        next_matched = compiled.split(next)
        nextnext_matched = compiled.split(nextnext)
        if len(curr_matched) == 10 and len(next_matched) and len(nextnext_matched) == 10:
            if curr_matched[1] == "名詞" and\
               next_matched[0] == "の" and\
               nextnext_matched[1] == "名詞":
                print ''.join([curr_matched[0],next_matched[0],nextnext_matched[0]]).decode('utf-8')
