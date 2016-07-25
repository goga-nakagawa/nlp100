#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
pattern = r"\t|\,"
compiled = re.compile(pattern)

with open('neko.txt.mecab') as f:
    freq = {}
    for line in f.readlines():
        matched = compiled.split(line)
        if matched and len(matched) == 10:
            if matched[0] in freq:
                freq[matched[0]] += 1
            else:
                freq[matched[0]] = 1
    sorted_list = [(k, v) for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
    for s in sorted_list:
        print s[0].decode('utf-8'), s[1]
