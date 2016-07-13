#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

pattern = r"^\|\s?(.*?)\s=\s(.*)"
compiled = re.compile(pattern)

with open("england.txt") as f:
    dic = {}
    for line in f.readlines():
        l = compiled.search(line)
        if l:
            dic[l.group(1)] = l.group(2)
    print dic