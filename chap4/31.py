#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
pattern = r"\t|\,"
compiled = re.compile(pattern)

with open('neko.txt.mecab') as f:
    for line in f.readlines():
        matched = compiled.split(line)
        if matched and len(matched) == 10:
            if matched[1] == "動詞":
                print matched[7].decode('utf-8')
