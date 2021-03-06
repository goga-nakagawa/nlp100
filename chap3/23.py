#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

pattern = r"^(=+)\s*(.*?)\s*(=+)$"
compiled = re.compile(pattern)

with open("england.txt") as f:
    for line in f.readlines():
        l = compiled.search(line)
        if l:
            print l.group(2), len(l.group(1))