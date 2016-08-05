#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
compiled = re.compile(r"^:\s(.*)$")
flg = False

with open("questions-words.txt", "rb") as infile:
    with open("family.txt", "wb") as outfile:
        for l in infile.readlines():
            if flg:
                outfile.write(l)
            m = compiled.match(l)
            if m:
                if m.group(1) == "family":
                    flg = True
                else:
                    flg = False