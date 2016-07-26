#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
ls = re.compile(r"^\n")
st = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")

with open("nlp.txt") as f:
    for l in f.readlines():
        if ls.match(l):
            continue
        else:
            sentences = st.split(l)
            for s in sentences:
                print s