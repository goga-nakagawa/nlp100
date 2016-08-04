#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

compiled = re.compile(r"[,\.:;!?\(\)\[\]\'\"]")

with open("enwiki-20150112-400-r100-10576.txt", "rb") as infile:
    with open("cleaned.txt", "wb") as outfile:
        for l in infile.readlines():
            outfile.write(re.sub(compiled, "", l))
