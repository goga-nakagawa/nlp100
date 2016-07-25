#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
pattern = r"\t|\,"
compiled = re.compile(pattern)

with open('neko.txt.mecab') as f:
    for line in f.readlines():
        matched = compiled.split(line)
        if matched and len(matched) == 10:
            if matched[1] == "名詞" and matched[2] == "サ変接続":
                print matched[0].decode('utf-8')
